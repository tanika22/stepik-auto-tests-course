from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    firstBtn = browser.find_element_by_xpath("//button[@type='submit']")
    firstBtn.click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

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

