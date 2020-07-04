from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = ''
password = ''

class faceBot:
	def __init__(self, username, password):
		driver = webdriver.Firefox()
		driver.get("https://www.facebook.com")
		driver.get_elements_from_xPath('<input xPath here>').send_keys(username)
		driver.get_elements_from_xPath('<input xPath here>').send_keys(password)
		driver.send_keys(Keys.ENTER)


username = input("Enter Username: ")
password = getpass("Enter password")
a = faceBot(username, password)

