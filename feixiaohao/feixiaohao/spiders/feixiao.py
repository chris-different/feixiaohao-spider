# -*- coding: utf-8 -*-
import scrapy
from ..items import FeixiaohaoItem

class FeixiaoSpider(scrapy.Spider):
    name = 'feixiao'
    allowed_domains = ['feixiaohao.com']
    start_urls = ['https://www.feixiaohao.com']

    def parse_info(self, response):
        feixiaohaoitem = FeixiaohaoItem()
        all_list = response.xpath('//div[@class="boxContain"]/table[@class="table maintable"]/tbody/tr//td/a/text()').extract()
        split_list = []
        for i in range(0,len(all_list),4):
            split_list.append(all_list[i:i+4])
        for i in split_list:
            feixiaohaoitem['name'] = i[1].strip()
            feixiaohaoitem['price'] = i[2].strip()
            feixiaohaoitem['market_price'] = i[3].strip()
            return feixiaohaoitem
        return feixiaohaoitem


    def parse(self, response):
        num_page = response.xpath('//div[@class="pageList"]/a/text()').extract()[-2]
        for i in range(1,int(num_page)+1):
            yield scrapy.Request(response.url+'/list_'+str(i)+'.html',callback=self.parse_info)
