# merge page
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes3'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for qt in response.css("div.quote"):
            text = qt.css("span::text").extract_first()
            author = qt.xpath(".//small/text()").extract_first()
            scraped_quote = {
                'text': text,
                'author': author,
                'birthday': None
            }
            author_href = qt.css(".author + a::attr(href)").extract_first()
            author_page = response.urljoin(author_href)
            yield scrapy.Request(author_page, meta={'item': scraped_quote}, callback=self.parse_author)

            next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)

    def parse_author(self, response):
        item = response.meta["item"]
        b = response.css(".author-born-date::text").extract_first().strip()
        item["birthday"] = b
        return item
