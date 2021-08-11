import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# 浏览器最大化
driver.maximize_window()

driver.find_element_by_id("kw").send_keys("张家齐")
driver.find_element_by_id("su").click()
# 浏览器长400px,宽1000px
time.sleep(3)
driver.set_window_size(400,1000)
time.sleep(3)
# js 实现浏览器滚动条到浏览器底端
js1 = "var q = document.documentElement.scrollTop=1000"
driver.execute_script(js1)
time.sleep(5)
# js 实现浏览器滚动条到浏览器顶端
js2 = "var q = document.documentElement.scrollTop=0"
driver.execute_script(js2)
time.sleep(5)
driver.quit()
