from selenium import webdriver
import time
from  selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:88/zentao/user-login-L3plbnRhby8=.html")
# 放大浏览器
driver.maximize_window()
driver.find_element_by_id("account").send_keys("admin")
# 用tab键定位焦点
name = driver.find_element_by_id("account")
name.send_keys(Keys.TAB)
time.sleep(4)
driver.find_element_by_name("password").send_keys("dwt7884347615")
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()