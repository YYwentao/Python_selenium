from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
# 拼 url
url = "file:///" + os.path.abspath("E:\\编程学习\\代码\\python\\Day1\\selenium2html\\drop_down.html")
driver.get(url)
driver.maximize_window()
time.sleep(3)
# 1.通过 tag name
options = driver.find_elements_by_tag_name("option")
for option in options:
    if option.get_attribute('value') == "10.69":
        option.click()
time.sleep(6)

# 2.通过 css selector
driver.find_element_by_css_selector("#ShippingMethod > option:nth-child(3)").click()
# 数组的方式去定位，操作
options[2].click()
time.sleep(6)
driver.quit()
