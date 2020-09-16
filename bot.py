from selenium import webdriver#webdriver main
from time import sleep#to pause
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import urllib.request
import pandas
from selenium.webdriver.chrome.options import Options
#import all the selenium packages


class Bot:
	def __init__(self, username, pw,headless=True):#logs in your account
		self.username = username#username
		self.password=pw#password
		options = Options()
		if headless:
			options.headless=True
		self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)#driver installed
		"""Lines above just set up everything we need"""

		self.driver.get('https://www.instagram.com/')#go to instagram.com
		sleep(2)#wait 1 second
		self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)#eneter username
		self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(pw)#eneter username
		self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()#hits enter
		sleep(5)#wait 3 seconds

		try:
			self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()#clicks on dont save
			sleep(2)
		except:
			pass

		try:
			self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()#clicks on dont turn off notifications
		except:
			pass
		"""Lines above login"""

	def get_followers_and_following(self,f,acc='me'):#gets a list of the people who follow you and who you or someone else follow
		if acc=='me':
			self.go_to_others_profile(self.username)
		else:
			go_to_others_profile(acc)
		try:
			if f=='followers':
				WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[2]'))).click()
				sleep(2)
			else:
				WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'))).click()
				sleep(2)
		except:
			return 'account is private'
		"""Goes to the the followers or following button"""


		scroll_box=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]')))#defines the box of the followers
		last_ht = 0
		ht=1
		while last_ht != ht:
			last_ht = ht
			sleep(3)
			ht = self.driver.execute_script("""
				arguments[0].scrollTo(0, arguments[0].scrollHeight);
				return arguments[0].scrollHeight;
				""", scroll_box)

		"""Lines above scroll through the box"""
		links = scroll_box.find_elements_by_tag_name('a')
		names = [name.text for name in links if name.text != '']#adds the names of the people to this list by extracting the name from the links

		self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()# close button
		self.driver.back()#go back
		self.driver.back()#go back
		self.driver.back()#go back
		return names#makes this function hold the value of the names

	def get_unfollowers(self,send_message=False):#gets the people that dont follow you back and has the option to send a message to them
		followers=self.get_followers_and_following('followers')#stores your followers
		following=self.get_followers_and_following('yedey')#stores people you follow
		trouble=[]
		for p in following:
			if p not in followers:
				trouble.append(p)
		print('Num of Followers: '+str(len(followers)))
		print('Num of Followers: '+str(len(following)))
		print('Unfollowers: '+str(trouble))
		print(len(trouble))
		if send_message:#requests to send a message
			for person in trouble:
				self.send_message(person,'You dont folow me back...nah jk im bored so i descided to make a bot that would send this to all the people that dont follow me back have a nice day')

		return trouble

	def send_message(self,follower,message,spam=1):#can send a message to someone
		WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a'))).click()#click on dm button on homepage
		WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button'))).click()#click compose message
		sleep(2)
		self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(follower)
		sleep(2)
		WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[2]/div[2]/div'))).click()
		sleep(2)
		WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[1]/div/div[2]/div/button'))).click()
		for i in range(spam):
			WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'))).send_keys(message)#type message
			WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button'))).click()
		self.driver.get('https://www.instagram.com/')

	def go_to_others_profile(self,person):#goes to a users profile
		x=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
		x.send_keys(person)
		WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]'))).click()

	def download_all_users_posts(self,acc):#downloaads all posts of a user
		driver=self.driver
		try:
			self.go_to_others_profile(acc)
		except:
			print('No accounts with the name '+acc+' were found.')
			return 'no accounts found'
		sleep(3)

		scroll_pause_time = 3

		# Get scroll height
		last_height = driver.execute_script("return document.body.scrollHeight")
		num=1
		dls=[]
		while True:
			sleep(3)
			x=self.driver.find_elements_by_class_name("FFVAD")

			for t in x:
				z=t.get_attribute('src')
				if z not in dls:
					dls.append(z)



			# Scroll down to bottom
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

			# Wait to load page
			sleep(scroll_pause_time)




			# Calculate new scroll height and compare with last scroll height
			new_height = driver.execute_script("return document.body.scrollHeight")
			if new_height == last_height:
				# If heights are the same it will exit the function
				break
			last_height = new_height

		q=1
		#downloads images
		for y in dls:
			try:
				urllib.request.urlretrieve(y, "s/"+acc+str(q)+'.jpg')
			except:
				print('No folder named s found. Create one the try again')
				return
			q+=1

		urllib.request.urlretrieve(self.download_profile_pic(acc), "s/"+acc+'pro_pic'+'.jpg')



		print("Done! Pictures in the s folder")

	def download_profile_pic(self,acc):#gets the profile picture of a user
		sleep(3)
		pro_pic=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div/span/img')
		src=pro_pic.get_attribute('src')
		return src
	

		


