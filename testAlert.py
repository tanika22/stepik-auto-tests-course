from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    startButton = browser.find_element_by_xpath("//button[@type='submit']")
    startButton.click()

    alert = browser.switch_to.alert
    alert.accept()

    input = browser.find_element_by_xpath("//span[@id='input_value']")
    x = input.text
    result = calc(int(x))
    answer = browser.find_element_by_xpath("//input[@id='answer']")
    answer.send_keys(result)

    btnSubmit = browser.find_element_by_xpath("//button[@type='submit']")
    btnSubmit.click()

finally:
    time.sleep(30)
    browser.quit()

