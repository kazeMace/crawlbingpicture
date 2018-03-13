import setting
import pymongo
import hashlib
import time
HOST = setting.DATABASE_HOST
PORT = setting.DATABASE_PORT
DB_NAME = setting.DB_NAME
COLLECTION_NAME = setting.COLLECTION_NAME
class ConnectionDataBase:

    def __init__(self):
        self.connection = pymongo.MongoClient(host=HOST, port=PORT)
        self.db = self.connection[DB_NAME]
        self.collection = self.db[COLLECTION_NAME]
        self.item_count = self.get_item_count()

    def get_item_count(self):
        all_count = self.collection.count()
        print(all_count)
        return all_count

    def get_item(self):
        items = self.collection.find()
        # for item in items:
        #     print(item)
        return items
    def to_hash(self, item):
        hash_string = item["description"] + item["date"] + item["location"] + item["picture_url"]
        hash = hashlib.sha1()
        hash.update(hash_string.encode('utf-8'))
        hash_code = hash.hexdigest()
        return hash_code

    def add(self, item):
        print(self.item_count)
        item["_id"] = self.item_count
        item["hash_code"] = self.to_hash(item)
        item["is_del"] = 0
        item["is_valid"] = 0
        item["push_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        if not self.check_repetition(item) :
            self.collection.insert(item)
        else:
            print("已经添加过了")

    def check_repetition(self, item):
        hash_string = item["description"] + item["date"] + item["location"] + item["picture_url"]
        hash = hashlib.sha1()
        hash.update(hash_string.encode('utf-8'))
        print(hash_string)
        hash_code = hash.hexdigest()
        if self.collection.find_one({'hash_code':hash_code}):
            return True
        else:
            return False


if __name__ == '__main__':
    c = ConnectionDataBase()
    c.get_item_count()