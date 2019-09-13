# -*- coding: utf-8 -*-
import scrapy

from ..items import SpaceItem
class Space1Spider(scrapy.Spider):
    name = 'space1'
    start_urls = ['http://spacy.io/api/']

    def parse(self, response):
        items=SpaceItem()
        #title=response.css("ul._5f8f49f4 li::text").extract()
        top_content=response.xpath("//ul[@class='_5f8f49f4']")
        for i in top_content:
            title=i.css("li::text").extract()
            sub_title=i.css("li a::text").extract()
            link=i.css("li a::attr(href)").extract()
            for j in range(0,len(link)):
                items['title']=title[0]
                items['sub_title']=sub_title[j]
                items['link']=link[j]

                yield items


