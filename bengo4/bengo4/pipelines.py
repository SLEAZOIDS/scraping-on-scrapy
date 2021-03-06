# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient  # mongoDB との接続
import datetime

class Bengo4Pipeline(object):

    def __init__(self, mongo_uri, mongo_db, mongolab_user, mongolab_pass):
        # インスタンス生成時に渡された引数で、変数初期化
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongolab_user = mongolab_user
        self.mongolab_pass = mongolab_pass

    @classmethod  # 引数にクラスがあるので、クラス変数にアクセスできる
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'), # settings.py て定義した変数にアクセスする
            mongo_db=crawler.settings.get('MONGO_DATABASE'),
            mongolab_user=crawler.settings.get('MONGOLAB_USER'),
            mongolab_pass=crawler.settings.get('MONGOLAB_PASS')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db.authenticate(self.mongolab_user, self.mongolab_pass)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db.self.mongo_db.update(
            {u'name': item['name']},
            {"$set": dict(item)},
            upsert = True
        )

        return item
