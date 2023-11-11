import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quote"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        self.logger.info("Início do scrape")
        for quote in response.css("div.quote"):
            text = quote.css(".text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("a.tag::text").getall()

            yield {
                "text": text,
                "author": author,
                "tags": tags,
            }

        self.logger.info("Busca da próxima página")
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            self.logger.info("Próxima página não encontrada")
