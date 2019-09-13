# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
class PytdocPipeline(object):
    def __init__(self):
        self.create_connection()
        #self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='xxxxxxxx',
            database='DBname'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS TBname""")
        self.curr.execute("""create table TBname(
                    title text,
                    link text

                )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into TBname values (%s,%s,%s)""", (
            item['title'],
            item['sub_title'],
            'https://docs.python.org/3/reference/' + item['link']
        ))
        self.conn.commit()
