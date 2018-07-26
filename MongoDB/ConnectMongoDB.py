# encoding = utf-8
import pymongo


class ConnectMongoDB(object):
    def __init__(self, host, port):
        self.conn = pymongo.MongoClient(
            host=host,
            port=port,
        )
        db = self.conn.admin
        collection = db.teacher
        collection.save({"name": "davieyang", "age": "99"})
        collection.insert({"name": "abc", "age": "98"})
        collection.insert({"name": "qq", "age": "97"})
        recordone = collection.find_one()
        recordonename = collection.find_one({"name": "qq"})
        recordoneage = collection.find_one({"age": "98"})
        print(recordone)
        print(recordonename)
        print(recordoneage)


if __name__ == '__main__':
    ConnectMongoDB(host='210.13.50.105', port=32037)
