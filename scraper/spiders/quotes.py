import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//div[@class="row"]/div[@class="col-md-8"]/div')
        for quote in quotes:
            q = quote.xpath('.//span[@class="text"]/text()').get()
            author = quote.xpath('.//small[@class="author"]/text()').get()
            yield {
                "Quote": q,
                "Author":author

            }
