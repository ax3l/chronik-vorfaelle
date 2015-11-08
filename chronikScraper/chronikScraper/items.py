# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChronikscraperItem(scrapy.Item):
    # define the fields for your item here like:

    title = scrapy.Field()
    date = scrapy.Field()
    
    city = scrapy.Field()
    state = scrapy.Field()

    source = scrapy.Field()

    injured = scrapy.Field()

    description = scrapy.Field()

    pass
