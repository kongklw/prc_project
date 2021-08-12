"""
读取kairosDB
"""
import os
import json
import base64

import requests
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor


class KDB:
    def __init__(self):
        self.address = "10.253.59.10:3001/ts"
        self.username = "test"
        self.password = "12345"
        self.headers = self.get_headers()

    def get_headers(self):
        user_pwd = self.username + ":" + self.password
        auth_str = base64.b64encode(user_pwd.encode("utf-8")).decode()
        return {"Authorization": "Basic " + auth_str}

    def get_tags(self, metric):
        rs = []
        try:
            url = f"http://{self.address}/api/v1/datapoints/query/tags"
            res = requests.post(url, headers=self.headers,
                                json={"metrics": [{"tags": {}, "name": metric}],
                                      "plugins": [], "cache_time": 0, "start_absolute": 0})
            if res.status_code == 200:
                rs = json.loads(res.text)
                if rs["queries"]:
                    rs = list(rs["queries"][0]["results"][0]["tags"].keys())
        except Exception as exc:
            print(exc)
        finally:
            return rs

    def group_by(self, metric, tag_lst, start_ts, end_ts):
        rs = []
        try:
            url = f"http://{self.address}/api/v1/datapoints/query"
            res = requests.post(url, headers=self.headers,
                                json={"metrics": [{"tags": {}, "name": metric,
                                                   "group_by": [{"name": "tag", "tags": tag_lst}],
                                                   "aggregators": [{"name": "sum", "sampling": {"value": "1",
                                                                                                "unit": "milliseconds"}}]}],
                                      "plugins": [], "cache_time": 0,
                                      "start_absolute": start_ts,
                                      "end_absolute": end_ts})
            if res.status_code == 200:
                res_d = json.loads(res.text)
                if res_d["queries"]:
                    rs = res_d["queries"][0]["results"]
        except Exception as exc:
            print(exc)
        finally:
            return rs


class Handler:
    @staticmethod
    def get_stat_d(all_lst):
        """
        将rest resp 整理成 需要的数据格式
        :param all_lst: [
                        {group_by: [{name: "tag", tags: ["target_name", "instance"],…}, {name: "type", type: "number"}]
                        name: "aiops.target.business"
                        tags: {instance: ["host2"], target_name: ["TimeIMSMOACK"]}}
                        values: [[1619681160000, 4], [1619681220000, 34]],
                        ...
                        ]
        :return: {"metric-tag1_v-tag2_v": [[ts, value],...]}
        """
        stat_d = {}
        for detail in all_lst:
            key_lst = [detail["name"]]
            tag_value_lst = [v[0] for v in detail["tags"].values()]
            key_lst.extend(tag_value_lst)
            key = "-".join(key_lst)
            stat_d[key] = detail["values"]
        return stat_d

    @staticmethod
    def write_file(stat_d, path):
        if not os.path.exists(path):
            os.makedirs(path)

        for key, value_lst in stat_d.items():
            if value_lst:
                with open(path + key + ".csv", encoding="utf8", mode="w") as f:
                    for each_v in value_lst:
                        ts, v = each_v
                        content = str(ts) + "," + str(v) + "\n"
                        f.write(content)


def main(metric, start_ts, end_ts, path):
    kdb = KDB()
    all_lst = kdb.group_by(metric, kdb.get_tags(metric), start_ts, end_ts)
    stat_d = Handler.get_stat_d(all_lst)
    Handler.write_file(stat_d, path)


if __name__ == "__main__":
    metric_lst = ["ebupt.cn.mobilecx.msg12_tps",
                  "ebupt.cn.mobilecx.msg12_nj_success_rate",
                  "ebupt.cn.mobilecx.msg12_dg_success_rate",
                  "ebupt.cn.mobilecx.msg12_nj_avg_latency",
                  "ebupt.cn.mobilecx.msg12_dg_avg_latency",
                  "ebupt.cn.mobilecx.msg23_tps",
                  "ebupt.cn.mobilecx.msg23_nj_success_rate",
                  "ebupt.cn.mobilecx.msg23_dg_success_rate",
                  "ebupt.cn.mobilecx.msg23_nj_avg_latency",
                  "ebupt.cn.mobilecx.msg23_dg_avg_latency",
                  "ebupt.cn.mobilecx.msg34_tps",
                  "ebupt.cn.mobilecx.msg34_nj_success_rate",
                  "ebupt.cn.mobilecx.msg34_dg_success_rate",
                  "ebupt.cn.mobilecx.msg34_nj_avg_latency",
                  "ebupt.cn.mobilecx.msg34_dg_avg_latency",
                  "ebupt.cn.mobilecx.msg45_tps",
                  "ebupt.cn.mobilecx.msg45_nj_success_rate",
                  "ebupt.cn.mobilecx.msg45_dg_success_rate",
                  "ebupt.cn.mobilecx.msg45_nj_avg_latency",
                  "ebupt.cn.mobilecx.msg45_dg_avg_latency",
                  "ebupt.cn.mobilecx.msg56_tps",
                  "ebupt.cn.mobilecx.msg56_nj_success_rate",
                  "ebupt.cn.mobilecx.msg56_dg_success_rate",
                  "ebupt.cn.mobilecx.msg56_nj_avg_latency",
                  "ebupt.cn.mobilecx.msg56_dg_avg_latency",
                  "ebupt.cn.mobilecx.msg67_tps",
                  "ebupt.cn.mobilecx.msg67_nj_success_rate",
                  "ebupt.cn.mobilecx.msg67_dg_success_rate",
                  "ebupt.cn.mobilecx.msg67_nj_avg_latency",
                  "ebupt.cn.mobilecx.msg67_dg_avg_latency",
                  "ebupt.cn.mobilecx.msg78_tps",
                  "ebupt.cn.mobilecx.msg78_nj_success_rate",
                  "ebupt.cn.mobilecx.msg78_dg_success_rate",
                  "ebupt.cn.mobilecx.msg78_nj_avg_latency",
                  "ebupt.cn.mobilecx.msg78_dg_avg_latency",
                  "ebupt.cn.mobilecx.whole_tps_address",
                  "ebupt.cn.mobilecx.whole_dg_success_rate",
                  "ebupt.cn.mobilecx.whole_nj_success_rate",
                  "ebupt.cn.mobilecx.whole_dg_avg_latency",
                  "ebupt.cn.mobilecx.whole_nj_avg_latency",
                  "ebupt.cn.czquery.msg12_tps",
                  "ebupt.cn.czquery.msg12_dg_success_rate",
                  "ebupt.cn.czquery.msg12_nj_success_rate",
                  "ebupt.cn.czquery.msg12_dg_avg_latency",
                  "ebupt.cn.czquery.msg12_nj_avg_latency",
                  "ebupt.cn.czquery.msg23_tps",
                  "ebupt.cn.czquery.msg23_dg_success_rate",
                  "ebupt.cn.czquery.msg23_nj_success_rate",
                  "ebupt.cn.czquery.msg23_dg_avg_latency",
                  "ebupt.cn.czquery.msg23_nj_avg_latency",
                  "ebupt.cn.czquery.msg34_tps",
                  "ebupt.cn.czquery.msg34_dg_success_rate",
                  "ebupt.cn.czquery.msg34_nj_success_rate",
                  "ebupt.cn.czquery.msg34_dg_avg_latency",
                  "ebupt.cn.czquery.msg34_nj_avg_latency",
                  "ebupt.cn.czquery.msg45_tps",
                  "ebupt.cn.czquery.msg45_dg_success_rate",
                  "ebupt.cn.czquery.msg45_nj_success_rate",
                  "ebupt.cn.czquery.msg45_dg_avg_latency",
                  "ebupt.cn.czquery.msg45_nj_avg_latency",
                  "ebupt.cn.czquery.msg56_tps",
                  "ebupt.cn.czquery.msg56_dg_success_rate",
                  "ebupt.cn.czquery.msg56_nj_success_rate",
                  "ebupt.cn.czquery.msg56_dg_avg_latency",
                  "ebupt.cn.czquery.msg56_nj_avg_latency",
                  "ebupt.cn.czquery.whole_tps_address",
                  "ebupt.cn.czquery.whole_dg_success_rate",
                  "ebupt.cn.czquery.whole_nj_success_rate",
                  "ebupt.cn.czquery.whole_dg_avg_latency",
                  "ebupt.cn.czquery.whole_nj_avg_latency",
                  "ebupt.cn.host.memory_usage",
                  "ebupt.cn.host.cpu_usage",
                  "ebupt.cn.host.eth_state",
                  "ebupt.cn.host.disk_io_read",
                  "ebupt.cn.host.file_system_usage",
                  "ebupt.cn.mq.enque_blocked_size",
                  "ebupt.cn.mq.enque_avg_latency"
                  "ebupt.cn.mq.enque_msg_count",
                  "ebupt.cn.mq.deque_msg_count",
                  "ebupt.cn.mq.enque_death_count",
                  "ebupt.cn.redis.latency",
                  "ebupt.cn.redis.tps",
                  "ebupt.cn.redis.memory_usage",
                  ]
    start_ts, end_ts = 1615510800000, 1615512600000
    path = "/app/aiops/EBAI/kdb_datas"
    with ThreadPoolExecutor(max_workers=cpu_count() * 2 + 2) as tp:
        [tp.submit(main, metric, start_ts, end_ts, path) for metric in metric_lst]
