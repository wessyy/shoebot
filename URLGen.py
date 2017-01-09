# http://www.adidas.com/us/nmd_xr1-primeknit-shoes/BB1967.html?forceSelSize=BB1967_570


def URLGen(modelName, modelNum, size):
	BaseSize = 580

	ShoeSize = size - 6.5
	ShoeSize = ShoeSize * 20
	RawSize = ShoeSize + BaseSize
	ShoeSizeCode = int(RawSize)

	URL = 'http://www.adidas.com/us/' + str(modelName) + '/' + str(modelNum) +'.html?forceSelSize=' + str(modelNum) + '_' + str(ShoeSizeCode)

	return URL

# ModelName = raw_input('Model Name ')
# ModelNum = raw_input('Model # ')
# Size = input('Size: ')

# URL = URLGen(ModelName, ModelNum, Size)

# print(str(URL))


	