# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class NationalFlagPipeline(object):
    def open_spider(self, spider):
        self.con = sqlite3.connect('national.sqlite')
        self.cu = self.con.cursor()

    def process_item(self, item, spider):
        insert_sql = "insert into nationdetail(national, national_all, state, capital, language, area, currency, area_code, general_situation , nation_flag_img_url,nation_flag_img_path) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(item['national'], item['national_all'], item['state'], item['capital'], item['language'], item['area'], item['currency'], item['area_code'], item['general_situation'], item['nation_flag_img_url'], item['nation_flag_img_path'])
        print(insert_sql)
        self.cu.execute(insert_sql)
        self.con.commit()
        return item

    def spider_close(self, spider):
         self.con.close()
