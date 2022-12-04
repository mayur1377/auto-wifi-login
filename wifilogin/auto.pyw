from selenium import webdriver
import os
import time

def startBot(username, password, url):
	path = "C:\wifilogin\\chromedriver"
	driver = webdriver.Chrome(path)
	driver.get(url)
	#connect window appears
	if(len(driver.window_handles)>1):
		driver.switch_to.window(driver.window_handles[1]) 
		time.sleep(0.1)
	driver.find_element("xpath", '//*[@id="details-button"]').click()
	time.sleep(0.1)
	driver.find_element("xpath", '//*[@id="proceed-link"]').click()
	time.sleep(0.1)
	driver.find_element("xpath", '/html/body/div/div/div[4]/div[1]/div[2]/div[1]/div[2]/div/div/input').send_keys(username)
	time.sleep(0.1)
	driver.find_element("xpath", '/html/body/div/div/div[4]/div[1]/div[2]/div[2]/div[2]/div/div/input').send_keys(password)
	time.sleep(0.1)
	driver.find_element("xpath", '/html/body/div/div/div[4]/div[2]/div').click()
	time.sleep(0.1)
	driver.find_element("xpath", '/html/body/div/div/div/div[3]/div/div/button').click()
	time.sleep(0.1)
with open("sample.txt") as f:
    username = f.readlines()[0].rstrip()
with open("sample.txt") as f:
    password = f.readlines()[1].rstrip()
url = "https://192.168.192.200/sonicui/7/login/#/?cid=-3"
startBot(username, password, url)





