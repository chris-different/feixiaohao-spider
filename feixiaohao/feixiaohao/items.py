# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FeixiaohaoItem(scrapy.Item):
    name = scrapy.Field()
    market_price = scrapy.Field()
    price = scrapy.Field()
    market_amount = scrapy.Field()
    count_amount = scrapy.Field()
    increase = scrapy.Field()

