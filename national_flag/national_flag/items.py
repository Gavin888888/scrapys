# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NationalFlagItem(scrapy.Item):
    # define the fields for your item here like:
    national = scrapy.Field()
    national_href = scrapy.Field()
    pass

class NationalDetailItem(scrapy.Item):
    # define the fields for your item here like:
    national = scrapy.Field()
    national_all = scrapy.Field()
    state = scrapy.Field()
    capital = scrapy.Field()
    language = scrapy.Field()
    area = scrapy.Field()
    currency = scrapy.Field()
    area_code = scrapy.Field()
    general_situation = scrapy.Field()
    nation_flag_img_url = scrapy.Field()
    nation_flag_img_path = scrapy.Field()
    pass
