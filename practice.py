Model = input('Model #: ')
Size = int(input('Size: '))
type = input('Shoe Name: ')

def URLGenSize(Model, Size, ShoeType):
    BaseSize = 530
    ShoeSize = new_func(Size)
    RawSize = ShoeSize + BaseSize
    ShoeSizeCode = int(RawSize)
    URL = 'https://www.adidas.com/us/' + str(type.replace(' ', '-')) + '/' + str(Model) + '.html?forceSelSize=' + str(Model) + '_' + str(ShoeSizeCode)
    return URL

def new_func(Size):
    ShoeSize = (Size - 4) * 20
    return ShoeSize


URL = URLGenSize(Model, Size, type)
print(URL)