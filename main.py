import webbrowser
import time
import scrapy
from typing import ItemsView
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

rules = ( Rule(LinkExtractor(restrict_xpaths='//a[contains(@class,"product-link")]',deny=('_[WM]\.html',)),
                callback='singleProductParse'),
            Rule(LinkExtractor(restrict_xpaths='//li[@class="pagging-arrow right-arrow"]'),
                follow=True))

class AdidasSpider(CrawlSpider):
    name = "adidas"
    allowed_domains = ["adidas.com"]
    start_urls = []
    def URLGenSize(self, Model, Size, type):
        BaseSize = 530
        ShoeSize = self.new_func(Size)
        RawSize = ShoeSize + BaseSize
        ShoeSizeCode = int(RawSize)
        URL = 'https://www.adidas.com/us/' + str(type.replace(' ', '-')) + '/' + str(Model) + '.html?forceSelSize=' + str(Model) + '_' + str(ShoeSizeCode)
        
        total_breaks = 1
        break_count = 0
        print("This program started on " + time.ctime())
        while(break_count < total_breaks):
        time.sleep(3)
        webbrowser.open(URL)
        break_count = break_count + 1
        return URL
      
    def new_func(self, Size):
        ShoeSize = (Size - 4) * 20
        return ShoeSize
      
    def URLplain(self, Model, type):
        urlplain = 'https://www.adidas.com/us/'  + str(type.replace(' ', '-')) + '/' + str(Model) + '.html'
        return urlplain
      
    def start_requests(self):
        Model = input('Model #: ')
        Size = int(input('Size: '))
        type = input('Shoe Name: ')
        URL = self.URLGenSize(Model, Size, type)
        urlplain = self.URLplain(Model, type)
        print(URL)
        print(urlplain)
        self.start_urls.append(URL)
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        price = response.css(".gl-price-item::text").get()
        print("SHOE PRICE =", price)

def CheckStock():
    process = CrawlerProcess()
    process.crawl(AdidasSpider)
    process.start()
CheckStock()


