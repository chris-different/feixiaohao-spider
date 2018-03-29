# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
import codecs
import json
import pymongo
class FeixiaohaoPipeline(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='127.0.0.1',port=6379)
    def process_item(self, item, spider):
        self.r.hmset(item['name'],
            {
            'f_id':item['f_id'],
            "name":item["name"],
            'flow_market_price':item['flow_market_price'],
            'price':item['price'],
            'flow_amount':item['flow_amount'],
            'trade_amount':item['trade_amount'],
            'price_change':item['price_change']
            })
        
        return item

class PingtaiPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient('127.0.0.1',27017)
        tdb = connection.alpha87
        self.post = tdb.test
    def process_item(self, item, spider):
        self.post.insert({'name':item['name'],'summary':item['summary'],'country':item['country'],'amount':item['amount']})
        return item




class MyPipeline(object):
    def __init__(self):
        self.file = codecs.open(
                'coin_price.json','w',encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ","
        self.file.write(line)
        return item
    def spider_close(self, spider):
        self.file.close()
