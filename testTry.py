from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_xpath("//span[@id='num1']")
    number1 = int(num1.text)
    num2 = browser.find_element_by_xpath("//span[@id='num2']")
    number2 = int(num2.text)
    result = str(number1 + number2)
    select = Select(browser.find_element_by_xpath("//select[@id='dropdown']"))
    select.select_by_value(result)
    submit = browser.find_element_by_xpath("//button[@type='submit']")
    submit.click()
    """x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_xpath("//input[@id='answer']")
    answer.send_keys(y)
    robotCheckbox = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    robotCheckbox.click()
    robotsRuleRadiobutton = browser.find_element_by_xpath("//input[@id='robotsRule']")
    robotsRuleRadiobutton.click()
    btnSubmit = browser.find_element_by_xpath("//button[@type='submit']")
    btnSubmit.click()"""

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла