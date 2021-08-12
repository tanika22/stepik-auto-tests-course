from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    input = browser.find_element_by_xpath("//span[@id='input_value']")
    x = input.text
    result = calc(int(x))
    answer = browser.find_element_by_xpath("//input[@id='answer']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(result)
    robotCheckbox = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
    robotCheckbox.click()
    robotRule = browser.find_element_by_xpath("//input[@id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotRule)
    robotRule.click()
    btnSubmit = browser.find_element_by_xpath("//button[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", btnSubmit)
    btnSubmit.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()


