import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scriptscraper.items import ScriptscraperItem

class LineSpider(CrawlSpider):
        name = 'lineSpider'
        allowed_domains = ['www.seinfeldscripts.com']
        start_urls = ['https://seinfeldscripts.com/alpha.html/']
        base_url = 'https://seinfeldscripts.com/'
        rules = ( 
      Rule(LinkExtractor(allow =(), restrict_xpaths = ("//div[@class = 'next']",)),callback = "parse_item", follow = True),)
    
def parse_item(self, response):
    item = ScriptscraperItem()
    item["link"] = response.xpath('//table/td/a/text()').extract()
    filename = 'links.html'
    with open(filename, 'wb') as f:
        f.write(response.body)
    self.log(f'Saved file {filename}')