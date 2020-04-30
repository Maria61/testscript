from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 组合键操作练习

driver.find_element_by_id("kw").send_keys("Ella")
driver.find_element_by_id("su").submit()
time.sleep(4)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")
time.sleep(4)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"x")
time.sleep(6)
driver.quit()

