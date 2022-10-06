import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scriptscraper.items import ScriptscraperItem

class LineSpider(CrawlSpider):
        name = "lineSpider"
        allowed_domains = ["seinfeldscripts.com"]
        start_urls = ["http://seinfeldscripts.com/alpha.html/"]
        base_url = "http://seinfeldscripts.com/"
        rules = [Rule(LinkExtractor(allow="/"), callback="parse_item", follow = True),]
        
def parse_item(self, response):
    item = ScriptscraperItem()
    hxs = Selector(response)
    l = ItemLoader(item,hxs)
    l.add_value('url',response.url)
    l.add_xpath('title', '//table/td/b/text()')
    l.add_xpath('link', '//table/td/a/@href')
    writeToFile(item)
    # item["link"] = response.xpath("//table/td/a/text()").extract()
    return l.load_item()


def writeToFile(e):
    filename = "links.txt"
    f = open(filename, 'w')
    f.write(e.get("link"))
    f.close()
    print(e)