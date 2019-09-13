# -*- coding: utf-8 -*-
import scrapy
from ..items import Req1Item

class FirstSpider(scrapy.Spider):
    name = 'first'
    #allowed_domains = ['https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html']
    start_urls = ['https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html']
    def parse(self, response):
        items=Req1Item()
        all_it=response.css('span.part')
        for i in all_it:
            sub_title=i.css("a::text").extract()
            link=i.css("a").xpath("@href").extract()
            items['title']='N'
            items['sub_title']=sub_title
            items['link']=link
            yield items

