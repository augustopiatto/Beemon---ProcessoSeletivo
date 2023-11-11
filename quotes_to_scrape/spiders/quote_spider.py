import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quote"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        filename = "quote"
        with open(filename, "wb") as f:
            f.write(response.body)
