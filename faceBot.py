from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time
import bcrypt

class faceBot:
	def __init__(self, username, password):
		driver = webdriver.Firefox()
		driver.get("https://www.facebook.com")
		driver.get_elements_from_xPath("//input[contains(@type,'email')]").send_keys(username)
		driver.get_elements_from_xPath("//input[@name='pass']").send_keys(password)
		driver.send_keys(Keys.ENTER)
	def hashing(self, password):
		salt = bcrypt.gensalt()
		hashed = bcrypt.hashpw(password, salt)
		

username = input("Enter Username: ")
password = getpass("Enter password")
a = faceBot(username, password)

