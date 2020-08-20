from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

#import our credentials from user input
import mainWindow

class faceBot:
	def __init__(self, username, password):
        username = mainWindow.username
        password = mainWindow.password
        driver = webdriver.Firefox()
        driver.get("https://www.facebook.com")
        driver.get_elements_from_xPath("//input[contains(@type,'email')]").send_keys(username)
        driver.get_elements_from_xPath("//input[@name='pass']").send_keys(password)
        driver.send_keys(Keys.ENTER)

username = input("Enter Username: ")
password = getpass("Enter password")
a = faceBot(username, password)

