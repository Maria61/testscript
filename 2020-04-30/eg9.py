from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('frame.html')
driver.get(file_path)

# 多层框架中的定位

driver.maximize_window()
driver.implicitly_wait(10)
# 定位到f1框架里
driver.switch_to.frame("f1")
# 定位到f2框架里
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("frame")
driver.find_element_by_id("su").submit()
time.sleep(4)
# 回到默认页面
driver.switch_to.default_content()
driver.switch_to.frame("f1")
driver.find_element_by_link_text("click").click()
time.sleep(4)
driver.quit()