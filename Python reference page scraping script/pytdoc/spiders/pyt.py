# -*- coding: utf-8 -*-
import scrapy

from ..items import PytdocItem
class PytSpider(scrapy.Spider):
    name = 'pyt'
    start_urls = ['http://docs.python.org/3/reference/index.html']

    def parse(self, response):
        item=PytdocItem()
        #top_lis=response.xpath("//li[@class='toctree-l1']/a[@class='reference internal']/text()").extract()
        top_lis=response.xpath("//li[@class='toctree-l1']")
        for i in top_lis:
            #title=i.xpath("//a[@class='reference internal']/text()").extract()
            title1=i.css("a::text").extract()
            link1=i.css("a::attr(href)").extract()
            for j in range(0,len(link1)):
                item['title']='N'
                item['sub_title']=title1[j]
                item['link']=link1[j]
                yield item


