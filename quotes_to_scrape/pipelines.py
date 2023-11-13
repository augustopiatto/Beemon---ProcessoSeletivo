# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import pymongo
from quotes_to_scrape import settings
import os
from datetime import datetime


class QuotesToScrapePipeline:
    def process_item(self, item, spider):
        return item


class MongoPipeline:
    def __init__(self):
        connection = pymongo.MongoClient(
            settings.MONGODB_HOST,
            settings.MONGODB_PORT,
            username=os.environ.get("MONGO_USERNAME", ""),
            password=os.environ.get("MONGO_PASSWORD", "")
        )
        db = connection[settings.MONGODB_DBNAME]
        self.collection = db[settings.MONGODB_COLLECTION_NAME]

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(settings.MONGODB_HOST)
        self.db = self.client[settings.MONGODB_DBNAME]
        self.items = []

    def close_spider(self, spider):
        if self.items:
            # Adiciona no banco
            self.insert_in_db()

        self.client.close()

    def process_item(self, item, spider):
        item["timestamp"] = datetime.now()
        self.items.append(item)
        if len(self.items) >= 100:
            self.insert_in_db()
            self.items = []

        return item
    
    def insert_in_db(self):
        self.collection.insert_many(self.items)
