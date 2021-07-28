Model = input('Model #: ')
Size = int(input('Size: '))
Type = input('Shoe Name: ')

def URLGenSize(Model, Size, ShoeType):
    BaseSize = 530
    ShoeSize = new_func(Size)
    RawSize = ShoeSize + BaseSize
    ShoeSizeCode = int(RawSize)
    URL = 'https://www.adidas.com/us/' + str(ShoeType) + '/' + str(Model) + '.html?forceSelSize=' + str(Model) + '_' + str(ShoeSizeCode)
    return URL

def new_func(Size):
    ShoeSize = (Size - 4) * 5
    return ShoeSize

def sillouette(Type):
    ShoeType = Type.replace(' ', '-')
    return ShoeType


URL = URLGenSize(Model, Size, Type)
print(URL)