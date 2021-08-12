import pymongo

mongo_con = ['mongodb://localhost:27017/', 'EB_AIOps2']
# mongo_con = ['mongodb://admin:123456@173.255.0.102:27017/', 'EB_AIOps2']

myclient = pymongo.MongoClient(mongo_con[0])
mydb = myclient[mongo_con[1]]

# data = mydb['index_alarm'].find()
# data = list(data)
# print(data)

# for item in data:
#     _id = item['_id']
#     index_name = item['index_name']

mydb['index_alarm'].update_many({}, {'$set': {'notice_method': '网管', 'index_level': 'P1'}})
