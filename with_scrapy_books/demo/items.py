# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    name = scrapy.Field()