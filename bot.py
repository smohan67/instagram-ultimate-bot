from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class InstaBot:
	def __init__(self, username, pw):#logs in your account
		self.username = username#username
		self.password=pw#password
		self.driver = webdriver.Chrome(ChromeDriverManager().install())#driver
		"""Lines above just set up everything we need"""

		self.driver.get('https://www.instagram.com/')#go to instagram.com
		sleep(2)#wait 1 second
		self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)#eneter username
		self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(pw)#eneter username
		self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]').click()#hits enter
		sleep(5)#wait 3 seconds

		try:
			self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
			sleep(2)
		except:
			pass

		try:
			self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
		except:
			pass
		"""Lines above login"""
	def get_followers_and_following(self):#gets a list of the people who follow you and who you follow
		sleep(1)
		self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
		sleep(1)
		self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div').click()
		"""Go to Profile"""








my_bot = InstaBot(username,password)#creates the bot based on your username and password
my_bot.get_followers_and_following()


myBot=Bot('siddmohann122','hello12345')

