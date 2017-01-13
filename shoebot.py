import requests
import bs4
import random
import webbrowser
from selenium import webdriver

# http://www.adidas.com/us/nmd_xr1-primeknit-shoes/BB1967.html?forceSelSize=BB1967_570


def URLGen(modelName, modelNum, size):
	baseSize = 580

	shoeSize = size - 6.5
	shoeSize = shoeSize * 20
	rawSize = shoeSize + baseSize
	shoeSizeCode = int(rawSize)

	URL = 'http://www.adidas.com/us/' + str(modelName) + '/' + str(modelNum) +'.html?forceSelSize=' + str(modelNum) + '_' + str(shoeSizeCode)

	return URL


def CheckStock(url, model):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	rawHTML = requests.get(url, headers = headers)
	page = bs4.BeautifulSoup(rawHTML.text, 'lxml')
	listofRawSizes = page.select('.size-dropdown-block')
	sizes = str(listofRawSizes[0].getText()).replace('\t', '')
	sizes = sizes.replace('\n\n', ' ')
	sizes = sizes.split()
	sizes.remove('Select')
	sizes.remove('size')

	for size in sizes:
		print(str(model) + 'Sizes: ' + str(size) + 'Available')


driver = webdriver.Chrome('venv/chromedriver-Darwin')
driver.get("http://www.adidas.com/us/nmd_xr1-primeknit-shoes/BB1967.html?forceSelSize=BB1967_570");
driver.find_element_by_css_selector('.btn-block').click()


def Main(model, size):
	url = URLGen(modelName, modelNum, size)
	CheckStock(url, model)



	