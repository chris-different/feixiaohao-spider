# -*- coding: utf-8 -*-
import scrapy
from ..items import PingtaiItem

class PingtaiSpider(scrapy.Spider):
    name = 'pingtai'
    start_urls = ['https://www.feixiaohao.com/exchange/']

    def parse_info(self, response):
        pingtaiitem = PingtaiItem()
        all_list = response.xpath('//ul[@class="plantList"]//li')
        for i in all_list:
            pingtaiitem['name'] = i.xpath('.//div[@class="tit"]/a/b/text()').extract_first().strip()
            pingtaiitem['summary'] = i.xpath('.//div[@class="des"]/text()').extract_first()
            pingtaiitem['country'] = i.xpath('.//div[@class="detal"]//a')[1].xpath('./text()').extract_first()
            pingtaiitem['amount'] = i.xpath('.//div[@class="detal"]//a')[4].xpath('./text()').extract_first()
            yield pingtaiitem 
    def parse(self, response):
        for i in range(1,15):
            yield scrapy.Request(response.url+'/list_'+str(i)+'.html',callback=self.parse_info)
