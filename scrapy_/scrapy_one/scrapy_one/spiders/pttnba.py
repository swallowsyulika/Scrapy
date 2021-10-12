# first sample
import scrapy


class PttnbaSpider(scrapy.Spider):
    name = 'pttnba'     # scrapy name, often mean the spider's name
    allowed_domains = ['ptt.cc']    # net domain
    start_urls = ['https://www.ptt.cc/bbs/NBA/index.html']     # url list

    def parse(self, response):      # main scrapy function
        titles = response.css("div.r-ent > div.title > a::text").extract()
        votes = response.xpath("//div[@class='nrec']/span/text()").extract()
        authors = response.xpath("//div[@class='meta']/div[1]/text()").extract()
        for ele in zip(titles, votes, authors):
            scraped_info = {
                "title": ele[0],
                "vote": ele[1],
                "author": ele[2]
            }
            yield scraped_info
