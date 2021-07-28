import scrapy
from typing import ItemsView
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


Model = input('Model #: ')
Size = int(input('Size: '))
type = input('Shoe Name: ')

def URLGenSize(Model, Size, type):
    BaseSize = 530
    ShoeSize = new_func(Size)
    RawSize = ShoeSize + BaseSize
    ShoeSizeCode = int(RawSize)
    URL = 'https://www.adidas.com/us/' + str(type.replace(' ', '-')) + '/' + str(Model) + '.html?forceSelSize=' + str(Model) + '_' + str(ShoeSizeCode)
    return URL

def new_func(Size):
    ShoeSize = (Size - 4) * 20
    return ShoeSize

def URLplain(Model, type):
    urlplain = 'https://www.adidas.com/us/'  + str(type.replace(' ', '-')) + '/' + str(Model)
    return urlplain
URL = URLGenSize(Model, Size, type)
urlplain = URLplain(Model, type)

print(URL)
print(urlplain)

rules = ( Rule(LinkExtractor(restrict_xpaths='//a[contains(@class,"product-link")]',deny=('_[WM]\.html',)),
                callback='singleProductParse'),
            Rule(LinkExtractor(restrict_xpaths='//li[@class="pagging-arrow right-arrow"]'),
                follow=True))

class AdidasSpider(CrawlSpider):
    name = "adidas"
    allowed_domains = ["adidas.com"]
    start_urls = [urlplain]

    def parse(self, response):
        l = ItemLoader(item = Product(), response=response)
        l.add_xpath('price', '//p[@id="price"]')
        l.add_css('stock', 'p#stock]')
        l.add_value('last_updated', 'today') # you can also use literal values
        return l.load_item()

def CheckStock():
    process = CrawlerProcess()
    process.crawl(AdidasSpider)   
    process.start()

print(CheckStock())

