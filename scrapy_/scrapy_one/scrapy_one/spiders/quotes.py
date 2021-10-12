# next page
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
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
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
