from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 设置浏览器窗口大小

time.sleep(6)
driver.maximize_window()
time.sleep(6)
driver.set_window_size(400,600)
time.sleep(6)
driver.quit()