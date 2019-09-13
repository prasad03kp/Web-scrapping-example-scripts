# -*- coding: utf-8 -*-
import scrapy
from ..items import TensorFlowItem
from scrapy.spiders import CrawlSpider

class TensorSpider(scrapy.Spider):
    name = 'tensor'
    start_urls = ['https://www.tensorflow.org/tutorials/']

    def parse(self, response):
        toplis=response.xpath("//li[@class='devsite-nav-item           devsite-nav-expandable           devsite-nav-accordion']/devsite-expandable-nav")
        print('length=------------------:'+str(len(toplis)))
        items=TensorFlowItem()
        for i in toplis:
            title=i.css("span::text").extract()
            tag=i.css("ul.devsite-nav-section li.devsite-nav-item a::attr(href)").extract()
            for k in range(1, len(tag)+1):

                    items['name']=title[0]
                    items['tag']=tag[k-1]
                    items['title']=title[k]
                    yield items
