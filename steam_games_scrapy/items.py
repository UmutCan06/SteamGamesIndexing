# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SteamGamesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    year = scrapy.Field()
    image = scrapy.Field()
    summary = scrapy.Field()
    tag = scrapy.Field()
    price = scrapy.Field()
    reviews = scrapy.Field()
    pass
