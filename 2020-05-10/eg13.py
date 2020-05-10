from selenium import webdriver
import time
import os

# alert相关处理——输入内容

driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('send.html')
driver.get(file_path)
time.sleep(4)

driver.find_element_by_tag_name("input").click()
time.sleep(4)
alert = driver.switch_to.alert
alert.send_keys("Maria")
time.sleep(4) #实际上这个停顿并不会看到key显示在输入框中
# alert.accept()
alert.dismiss()
time.sleep(4)
driver.quit()