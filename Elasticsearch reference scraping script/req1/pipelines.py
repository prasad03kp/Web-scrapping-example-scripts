# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
class Req1Pipeline(object):
    def __init__(self):
        self.create_connection()
        self.curr.execute("""delete from space where title='N'""")

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
        self.curr.execute("""create table TBname (
                    title text,
                    link text

                )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into TBname values (%s,%s,%s)""", (
            item['title'][0],
            item['sub_title'][0],
            'https://www.elastic.co/guide/en/elasticsearch/reference/current/'+ item['link'][0]
        ))
        self.conn.commit()
