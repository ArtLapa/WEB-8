import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        items = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            yield items

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
