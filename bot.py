from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Imports the nessary modules


PATH=r'C:\Users\siddhu\chromedriver.exe'
driver=webdriver.Chrome(PATH)
#Initializes the chromedriver

class Bot():
    def __init__(self,username,password):
        self.username=username
        self.password=password
        driver.get("https://www.instagram.com/")#goes to the website
        time.sleep(2)#waits 2 seconds
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)#enter username
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password)#enter password
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()#clicks enter button
        time.sleep(4)#wait 4 seconds
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()#clicks not now
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()#clicks not now for notifictactions
    def get_following(self):
        following=[]
        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()#go to profile pic
        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div').click()#go to profile
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()#clicks on following




myBot=Bot('siddmohann122','hello12345')
myBot.get_following()
