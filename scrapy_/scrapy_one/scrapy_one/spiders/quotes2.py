# next page other way
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes2'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for qt in response.css("div.quote"):
            text = qt.css("span::text").extract_first()
            author = qt.xpath(".//small/text()").extract_first()
            scraped_quote = {
                'text': text,
                'author': author
            }
            yield scraped_quote
        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
