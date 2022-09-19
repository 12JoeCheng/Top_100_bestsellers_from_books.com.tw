import scrapy
from ..items import DemoItem


class DemospiderSpider(scrapy.Spider):
    name = 'demospider'
    user_agent =  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    start_urls = ['https://www.books.com.tw/web/sys_tdrntb/books/?loc=menu_th_1_001']



    def parse(self, response):
        items = DemoItem()

        for products in response.css('li.item'):
            link = products.css('div.type02_bd-a').css('h4').css('a::attr(href)').get()
            author = products.css('ul.msg').css('li').css('a::text').get()
            price = products.css('li.price_a').css('strong')[1::2].css('b::text').get()
            name = products.css('div.type02_bd-a').css('h4').css('a::text').get()

            items['link'] = link
            items['author'] = author
            items['price'] = price
            items['name'] = name

            yield items
        
