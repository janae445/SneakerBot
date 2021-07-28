#https://www.adidas.com/us/nmd_r1-shoes/GX0997.html?forceSelSize=GX0997_580
def URLGen(Model, Size):
    BaseSize = 580
    ShoeSize = new_func(Size)
    RawSize = ShoeSize + BaseSize
    ShoeSizeCode = int(RawSize)
    URL = 'https://www.adidas.com/us/' + str(Type) + '/' + str(Model) + '.html?forceSelSize=' + str(Model) + '_' + str(ShoeSizeCode)
    return URL

def new_func(Size):
    ShoeSize = Size - 6.5
    ShoeSize = Size * 5
    return ShoeSize

def shoe_type(Type):
    ShoeType = Type.replace(' ', '-')

Model = input('Model #: ')
Size = int(input('Size: '))
Type = input('Shoe Type: ')

URL = URLGen(Model, Size)
print(str(URL))




