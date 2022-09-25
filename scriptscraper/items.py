# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScriptscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    speaker = scrapy.Field()
    line = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
    pass
