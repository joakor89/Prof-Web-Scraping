import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://toscrape.com'
    ]
    
    def parse(self, response):
        with open('results.html', 'w', encoding = 'utf-8') as f:
            f.write(response.text)