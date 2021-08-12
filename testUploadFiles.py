import os
import time

from selenium import webdriver

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    firstName = browser.find_element_by_xpath("//input[@name='firstname']")
    firstName.send_keys("FirstName")
    lastName = browser.find_element_by_xpath("//input[@name='lastname']")
    lastName.send_keys("LastName")
    email = browser.find_element_by_xpath("//input[@name='email']")
    email.send_keys("test@test.com")
    #uploading file
    upload = browser.find_element_by_xpath("//input[@type='file']")
    upload.send_keys("D:\Training\Test.txt")
    #submit form
    btnSubmit = browser.find_element_by_xpath("//button[@type='submit']")
    btnSubmit.click()
finally:
    time.sleep(30)
    browser.quit()


