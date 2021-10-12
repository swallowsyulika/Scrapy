# setting FEED
import scrapy
from ..items import NBAItem     # remember import

class PttnbaSpider(scrapy.Spider):
    name = 'pttnba'
    allowed_domains = ['ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/NBA/index.html']

    def parse(self, response):
        for ele in response.css(".r-ent"):
            item = NBAItem()
            item['title'] = ele.css("div.title > a::text").extract_first()
            item['vote'] = ele.xpath("./div[@class='nrec']/span/text()").extract_first()
            item['author'] = ele.xpath("./div[@class='meta']/div[1]/text()").extract_first()
            yield item
