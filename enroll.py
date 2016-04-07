import re, sys, sched, datetime, urllib, urllib2, urlparse, getpass
import time as timeModule
from datetime import datetime,date,timedelta,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Registration')))
	driver.implicitly_wait(2)
	driver.find_element_by_link_text("Registration").click()

	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'bookbag')))
	driver.implicitly_wait(2)
	driver.find_element_by_link_text("bookbag").click()

	waitTime = datetime(2016, 4, 7, 7, 0, 0, 0) - datetime.today()
	if (waitTime.total_seconds()>0):
		print 'Waiting to check in for '+  str(waitTime)
		timeModule.sleep(waitTime.total_seconds())

	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Go To Enroll Page')))
	driver.find_element_by_link_text("Go To Enroll Page").click()

	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Go To Enroll Page')))
	driver.find_element_by_link_text("Finish Enrolling").click()