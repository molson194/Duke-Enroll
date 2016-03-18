import re, sys, sched, datetime, urllib, urllib2, urlparse, getpass
import time as timeModule
from datetime import datetime,date,timedelta,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
	username = raw_input("Username: ")
	password = getpass.getpass('Password: ')

	driver = webdriver.Chrome('/Users/Olson/Downloads/chromedriver')
	driver.get('https://aces.duke.edu')

	elem1 = driver.find_element_by_name('j_username')
	elem1.send_keys(username)
	elem2 = driver.find_element_by_name('j_password')
	elem2.send_keys(password)
	driver.find_element_by_name('Submit').click()

	driver.find_element_by_link_text("Registration").click()