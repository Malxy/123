from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import telegram_send
import time

PATH = "root/123/chromedriver"
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
n = 0
telegram_send.send(messages=["Starting .."])
while 1:
	driver = webdriver.Chrome(PATH,options=chrome_options)
	driver.get("https://altex.ro/console-ps5/cpl/")
	time.sleep(1)
	try:
		element= driver.find_element_by_css_selector("#__next > div.u-container > main > div.u-clearfix > div.lg\:mt-8 > div.border.flex.items-center.text-usm.p-3.rounded.text-alertYellow.bg-alertYellow-bg.border-alertYellow-border > div").text
		print(element)

	except:
		telegram_send.send(messages=["TIMEOUT"])
		telegram_send.send(messages=["https://altex.ro/console-ps5/cpl/"])
		print("no.")

	n=n+1

	
	print("Tried",n,"times")
	time.sleep(10)
	driver.quit()
