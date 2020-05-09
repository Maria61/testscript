from selenium import webdriver
import time
import os

# alert、confirm、prompt的处理

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('alert.html')
driver.get(file_path)
time.sleep(4)

driver.find_element_by_id("tooltip").click() #submit()不可以？why?
time.sleep(5)
# 从当前页面转向 alert 页面进行定位
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(4)
driver.quit()

