import requests
import bs4
import webbrowser
import random
import csv
import threading
import RandomHeaders

ModelNumber = 'GX0997'
SizeList = [7, 7.5, 8, 8.5]
ThreadCount = 10

def DoSomething():
	print('I just did something')

def URLGen(Model, Size, ShoeType):
    BaseSize = 580
    ShoeSize = new_func(Size)
    RawSize = ShoeSize + BaseSize
    ShoeSizeCode = int(RawSize)
    URL = 'https://www.adidas.com/us/' + str(ShoeType) + '/' + str(Model) + '.html?forceSelSize=' + str(Model) + '_' + str(ShoeSizeCode)
    return URL

def new_func(Size):
    ShoeSize = Size - 6.5
    ShoeSize = Size * 5
    return ShoeSize

def shoe_type(Type):
    ShoeType = Type.replace(' ', '-')
    return ShoeType

Model = input('Model #: ')
Size = int(input('Size: '))
Type = input('Shoe Type: ')

URL = URLGen(Model, Size, Type)

def CheckStock(URL):
	headers = {'User-Agent': random.choice('UserAgent')}
	RawHTML = requests.get(URL, headers=headers)
	Page = bs4.BeautifulSoup(RawHTML.text, "lxml")
	ListOfRawSizes = Page.select('.size-dropdown-block')
	Sizes = str(ListOfRawSizes[0].getText()).replace('\t', '')
	Sizes = Sizes.replace('\n\n', ' ')
	Sizes = Sizes.split()
	Sizes.remove('Select')
	Sizes.remove('size')
	for Size in Sizes:
		print(str(Model) + ' Size: ' + str(Size) + ' Available')

def Main(Model, Size):
	url = URLGen(Model, Size, Type)
	CheckStock(url, Model)

def SneakerBot(Model, size=None):
	while True:
		try:
			url = 'http://www.adidas.com/us/{}/{}.html?'.format(Type, Model)
			Sizes = CheckStock(url)
			if size != None:
				#If you didn't input size
				if str(size) in Sizes:
					DoSomething()
			else:
				for a in Sizes:
					DoSomething()
		except:
			pass

threads = [threading.Thread(name='ThreadNumber{}'.format(n), target=SneakerBot, args = (ModelNumber, size,)) for size in SizeList for n in range(ThreadCount)]
for t in threads: t.start()