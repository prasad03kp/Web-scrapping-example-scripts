# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PytdocItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sub_title=scrapy.Field()
    title=scrapy.Field()
    link=scrapy.Field()
