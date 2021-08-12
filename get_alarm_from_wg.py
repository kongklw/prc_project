"""
对接网管告警数据，并入库mongo
"""

import json
import time
import pytz
import datetime
import pymongo
import requests
import traceback
from bidict import bidict
from functools import wraps
from threading import Thread
from queue import Queue, Full, Empty

MONGO_USER = "developer"
MONGO_PASSWORD = 123456
MONGO_IP_PORT = "10.1.69.4:27017"
MONGO_DEFAULT_KEYSPACE = "EB_AIOps"
MONGO_ALERT_COLLECTION = "alarm_org_data"
WG_REQ_URL = "http://10.212.21.3:7080/v1/omsalarm/activealarm"


def run_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            raise e
        finally:
            end = time.perf_counter()
            print(str(func.__name__) + " Run Time: " + str(end - start))

    return wrapper


class MyMongo:
    def __init__(self):
        self.__client = pymongo.MongoClient("mongodb://{user}:{pwd}@{ip_port}/?"
                                            "authSource=admin&readPreference=primary&"
                                            "appname=MongoDB%20Compass&ssl=false".format(user=MONGO_USER,
                                                                                         pwd=MONGO_PASSWORD,
                                                                                         ip_port=MONGO_IP_PORT),
                                            connect=False)
        self.__db = self.__client[MONGO_DEFAULT_KEYSPACE]
        self.__collection = MONGO_ALERT_COLLECTION

    def exist_record(self, alarm_id):
        return self.__db[self.__collection].find_one({"alarm_id": alarm_id}, sort=[("_id", -1,)])

    def insert_many(self, data_list):
        res = self.__db[self.__collection].insert_many(data_list) if data_list else None
        return res

    def update_record(self, alarm_id, data_dict):
        rs = self.__db[self.__collection].update_one({"alarm_id": alarm_id}, {"$set": data_dict})
        return rs.modified_count

    def close(self):
        self.__client.close()


class RemoteCall:
    def __init__(self):
        self.__url = WG_REQ_URL

    @run_time
    def call(self, url=None):
        if url is None:
            url = self.__url
        session = requests.session()
        req_kwargs = {"method": "GET", "url": url, "json": {},
                      "headers": {"Content-Type": "application/json"}}
        response = session.request(**req_kwargs)
        return json.loads(response.text) if response.status_code == 200 else {}


class TimeConverter:
    @staticmethod
    def convert2ms(timestamp):
        if isinstance(timestamp, str):
            timestamp = int(timestamp)
        return int(timestamp * 1000)

    @staticmethod
    def get_ts_by_dt_str(dt_str):
        try:
            # dt_str to dt
            dt = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
            # dt to ts
            tz = pytz.timezone('Asia/Shanghai')
            t = tz.localize(dt)
            t = t.astimezone(pytz.utc)
            ts = int(time.mktime(t.utctimetuple())) - time.timezone
            return TimeConverter.convert2ms(ts)
        except Exception as e:
            return None


class FieldConverter:
    def __init__(self):
        self.my_mongo = MyMongo()
        self._mapper = bidict({'src_clu': 'cluster_name',
                               'src_host': 'computer_name',
                               'src_acc': 'account',
                               'alarm_code': 'alarm_code',
                               'title': 'alarm_title',
                               'cause': 'alarm_reason',
                               'solve': 'alarm_handle',
                               'alarmtype': 'alarm_class',
                               'instance': 'alarm_exp',
                               'alarm_level': 'alarm_level',
                               'dev_first_time': 'alarm_occur_time',
                               'dev_time': 'alarm_update_time',
                               'count': 'alarm_count',
                               'clear_status': 'alarm_clean_status',
                               'clear_time': 'alarm_clean_time',
                               'alarm_id': 'alarm_id'})

        self._handler = {'alarm_level': FieldConverter.convert_level,
                         'dev_first_time': TimeConverter.get_ts_by_dt_str,
                         'dev_time': TimeConverter.get_ts_by_dt_str,
                         'clear_status': FieldConverter.convert_status,
                         'clear_time': TimeConverter.get_ts_by_dt_str}

    @staticmethod
    def convert_level(level):
        level_mapper = {"4": "信息", "3": "警告", "2": "次要", "1": "重要", "0": "紧急"}
        return level_mapper.get(level)

    @staticmethod
    def convert_status(status):
        status_mapper = {"0": "未清除", "1": "已清除"}
        return status_mapper.get(status)

    def update_already_exist(self, alarm_id, alarm):
        flag = False
        exist = self.my_mongo.exist_record(alarm_id)
        if exist:
            del exist["_id"]
            if exist != alarm:
                res = self.my_mongo.update_record(alarm_id, alarm)
                print("modify_res:", res, " alarm_id: ", alarm_id)
            flag = True
        return flag

    def get_converted_list(self, alarm_list):
        converted_list = []
        for alarm in alarm_list:
            converted_dict = {}
            for new_field in self._mapper.inverse.keys():
                old_field = self._mapper.inverse.get(new_field)
                value = alarm.get(old_field)
                converted_dict[new_field] = self._handler[old_field](value) if old_field in self._handler else value

            alarm_id = alarm.get("alarm_id")
            if not self.update_already_exist(alarm_id, converted_dict):
                converted_list.append(converted_dict)
        return converted_list


my_mongo = MyMongo()
remote_call = RemoteCall()
field_converter = FieldConverter()


@run_time
def data2mango(alarm_list):
    try:
        converted_list = field_converter.get_converted_list(alarm_list)
        data_list = sorted(converted_list, key=lambda x: x['alarm_occur_time'], reverse=False)
        my_mongo.insert_many(data_list)
    except Exception as e:
        print(traceback.format_exc())


def producer(q):
    while True:
        try:
            if q.qsize() > 100:
                print("data accumulation over 100...")
            alarm_list = remote_call.call().get("alarmEventList")
            q.put_nowait(alarm_list)
        except Full as exc:
            print("queue is Full...")
            # 做点什么保存可能丢失的告警


def consumer(q):
    while True:
        try:
            alarm_list = q.get_nowait()
            data2mango(alarm_list)
        except Empty as exc:
            # print("queue is Empty...")
            continue


def execute_loop():
    q = Queue()
    producer_task = Thread(target=producer, args=(q,))
    thread_list = [producer_task]
    for i in range(3):
        consumer_task = Thread(target=consumer, args=(q,))
        thread_list.append(consumer_task)

    for thread in thread_list:
        thread.start()


def execute_once():
    alarm_list = remote_call.call().get("alarmEventList")
    data2mango(alarm_list)


if __name__ == "__main__":
    execute_loop()
