# -*- coding: utf-8 -*-
import scrapy
from ..items import FeixiaohaoItem

class FeixiaoSpider(scrapy.Spider):
    name = 'feixiao'
    start_urls = ['https://www.feixiaohao.com']
    

    def parse_info(self, response):
        feixiaohaoitem = FeixiaohaoItem()
        all_list = response.xpath('//div[@class="boxContain"]/table[@class="table maintable"]/tbody//tr')
        for i in all_list:

            feixiaohaoitem['f_id'] = i.xpath('.//td')[0].xpath('./text()').extract_first().strip()
            feixiaohaoitem['name'] = i.xpath('.//td')[1].xpath('./a/text()').extract()[1].strip()
            feixiaohaoitem['flow_market_price'] = i.xpath('.//td')[2].xpath('./text()').extract_first().strip()
            feixiaohaoitem['price'] = i.xpath('.//td')[3].xpath('./a/text()').extract_first().strip()
            feixiaohaoitem['flow_amount'] = i.xpath('.//td')[4].xpath('./text()').extract_first().strip()
            feixiaohaoitem['trade_amount'] = i.xpath('.//td')[5].xpath('./a/text()').extract_first().strip()
            feixiaohaoitem['price_change'] = i.xpath('.//td')[6].xpath('./span/text()').extract_first().strip()
            yield feixiaohaoitem


    def parse(self, response):
            
        for i in range(1,3):
            yield scrapy.Request(response.url+'/list_'+str(i)+'.html',callback=self.parse_info)
