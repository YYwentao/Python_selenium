import time

from selenium import webdriver
drive = webdriver.Chrome()
drive.get("https://www.baidu.com/")
# drive.find_element_by_id("kw").send_keys("东京奥运会")
# drive.find_element_by_id("su").click()
# drive.find_element_by_css_selector("#kw").send_keys("马龙")
# drive.find_element_by_css_selector("#su").click()

# text = drive.find_element_by_xpath("//*[@id='bottom_layer']/div").text
# print(text)

drive.find_element_by_id("kw").send_keys("你好，世界")
drive.find_element_by_id("su").click()
time.sleep(5)
drive.find_element_by_id("kw").clear()
time.sleep(5)
drive.find_element_by_id("kw").send_keys("马龙")
drive.find_element_by_id("su").submit()
time.sleep(8)
drive.quit()