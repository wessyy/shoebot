import requests
import bs4
import random
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys




def URLGen(modelNum, size, captchaCode=''):
	baseSize = 580

	shoeSize = size - 6.5
	shoeSize = shoeSize * 20
	rawSize = shoeSize + baseSize
	shoeSizeCode = int(rawSize)

	URL = 'http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-MiniAddProduct?pid=' + str(modelNum) + '_' + str(shoeSizeCode) + '&masterPid=&ajax=true&g-recaptcha-response=' + captchaCode

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


def AddToCart(url):
	driver = webdriver.Chrome('venv/chromedriver-Darwin')
	driver.get(url)
	driver.find_element_by_link_text('1').click()



def CaptchaKeyGen():
	driver = webdriver.Chrome('venv/chromedriver-Darwin')
	driver.get('http://www.adidas.com/us/nmd_r1-primeknit-shoes/BY1888.html?forceSelSize=BY1888_670')
	checkbox = WebDriverWait(driver).until(expected_conditions.presence_of_element_located((By.ID, 'recaptcha-anchor')))
	token_element = driver.find_element_by_id('g-recaptcha-response')
	token = token_element.get_attribute('value')
	
	sitekey = driver.find_element_by_class_name('g-recaptcha').get_attribute('data-sitekey')
	
	








# Generate a captcha key by pressing captcha and using captcha key code
# Then click cart and inspect continue shopping button, add this url into action:
# Press continue
# Go to link


# http://www.adidas.com/on/demandware.store/Sites-adidas-US-Site/en_US/Cart-MiniAddProduct?pid=BA7245_670&masterPid=&ajax=true&g-recaptcha-response=03AI-r6f63SL7hCXSRNrtVBU99fwsUm6CiwJYkGvcsOD7jaYczgNnuOE3eboxkr2WYtZqxGoqVr-J-NXmhoj2_kuWVaOcmNGlmp0knTVZdDuLR_FyDUs5hmj39sjT7tN3-3LopWYsLxHer2CZ0J6dQeq6SYasfAPSnw-sqCVVvZbfEI488k9zOk2kVL_tc6MoOmU-vabZSsG2v4duUHk97TPdOazBP3pZ0glnlYzp0Zg0_1xcLULQ01-noPsEec4Qk7R_r7rEj9S0wkLDxWam5zu7JUCLV4JwraYNExHI_eMX1Suj2jA6baKgqQA3ibSuWgDRoKYum4F9cxEBTHA0ZaUVuDpg0WSnprXG1VJMEC_yWGVW2JPi6-RBwnAwpNHqfMOn6odQSfJrHf7yppRn3TAKVjs8rVykdyqKNuA8GH1GUxlQTIBPeAzc

# javascript:prompt("Press CMD+C (Mac) or CTRL+C (Win)", $('.g-recaptcha').attr('data-sitekey'));
# document.getElementById('g-recaptcha-response').value

# python manage.py runserver
# http://127.0.0.1:8000/interface/


# 6Le4AQgUAAAAAABhHEq7RWQNJwGR_M-6Jni9tgtA
	