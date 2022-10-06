from scrapy.item import Item, Field


class ScriptscraperItem(Item):
    link = Field()
    title = Field()
    speaker = Field()
    line = Field()
    pass