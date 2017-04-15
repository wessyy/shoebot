import shoebot
import time


if __name__ == '__main__':
	driver = shoebot.webdriver.Chrome('venv/chromedriver-Darwin')
	driver.get('http://127.0.0.1:8000/interface/')

	trigger = 'Loading'
	running_counter = 0
	while True:
		# When user clicks Submit, button text will change to "Loading"
		print 'Running again'
		while driver.find_element_by_id('submit1').get_attribute('value') != trigger:
			time.sleep(0.5)

		# Extract entered values from field
		model_num = driver.find_element_by_id("Model Number").get_attribute('value')
		size = float(driver.find_element_by_id("Size").get_attribute('value'))
		captcha_token = driver.find_element_by_id("CAPTCHA_token").get_attribute('value')

		# Generate backdoor link
		url = shoebot.URLGen(model_num, size, captcha_token)
		print model_num
		print size
		print captcha_token
		print url

		# Open new tab
		window_before = driver.window_handles[0]
		driver.execute_script("window.open('');")
		window_after = driver.window_handles[running_counter + 1]
		driver.switch_to_window(window_after)

		# Go to link
		driver.get(url)
		try:
			driver.find_element_by_link_text('1').click()
		except:
			# Not always the case, sometimes if more than 1 in cart will have hyperlink '2'
			print "Couldn't add to cart. Try again"

		# Switch back control to submit window
		driver.switch_to_window(window_before)

		# Reload
		trigger = 'Submit' if trigger == 'Loading' else 'Loading'
		running_counter += 1

		time.sleep(0.5)






	