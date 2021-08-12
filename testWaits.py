from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(2)
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    btnBook = browser.find_element_by_xpath("//button[@id='book']")
    btnBook.click()

    x = browser.find_element_by_xpath("//span[@id='input_value']")
    result = int(x.text)
    answer = calc(result)
    inputAnswer = browser.find_element_by_xpath("//input[@id='answer']")
    inputAnswer.send_keys(answer)

    btnSubmit = browser.find_element_by_xpath("//button[@type='submit']")
    btnSubmit.click()

finally:
    time.sleep(30)
    browser.quit()




