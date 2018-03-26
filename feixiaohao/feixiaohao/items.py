# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FeixiaohaoItem(scrapy.Item):
    f_id = scrapy.Field()
    name = scrapy.Field()
    flow_market_price = scrapy.Field()
    price = scrapy.Field()
    flow_amount = scrapy.Field()
    trade_amount = scrapy.Field()
    price_change = scrapy.Field()

