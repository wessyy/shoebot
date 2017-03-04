import shoebot
import time


if __name__ == '__main__':
	driver = shoebot.webdriver.Chrome('venv/chromedriver-Darwin')
	driver.get('http://127.0.0.1:8000/interface/')

	# When user clicks Submit, button text will change to "Loading"
	while driver.find_element_by_id('submit1').get_attribute('value') != 'Loading':
		time.sleep(0.5)

	# Extract entered values from field
	model_num = driver.find_element_by_id("Model Number").get_attribute('value')
	size = float(driver.find_element_by_id("Size").get_attribute('value'))
	captcha_token = driver.find_element_by_id("CAPTCHA_token").get_attribute('value')

	# Generate backdoor link
	url = shoebot.URLGen(model_num, size, captcha_token)

	# Open new tab
	window_before = driver.window_handles[0]
	driver.execute_script("window.open('');")
	window_after = driver.window_handles[1]
	driver.switch_to_window(window_after)
	
	# Go to link
	driver.get(url)
	driver.find_element_by_link_text('1').click()




	