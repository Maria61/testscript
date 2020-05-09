from selenium import webdriver
import time
import os
from selenium.webdriver.common.action_chains import ActionChains

# 下拉框定位：下拉框即按钮点击后，选择其中的一个选项并显示在下拉框中
# TODO:思考下拉框定位和层级定位的区别？ActionChains的适用场景？


driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('drop_down.html')
driver.get(file_path)
time.sleep(6)

# ships = driver.find_element_by_id("ShippingMethod")
# time.sleep(4)
# ships.find_element_by_xpath("//*[@id='ShippingMethod']/option[3]").click()
# time.sleep(4)
# ships.find_element_by_xpath("//*[@value = '9.03']").click()

options = driver.find_element_by_id("ShippingMethod").find_elements_by_tag_name("option")
driver.implicitly_wait(10)
# ActionChains(driver).move_to_element(options[0]).perform() #有问题，运行报错
for option in options:
    if option.get_attribute('value') == '9.25':
        option.click()

time.sleep(6)
driver.quit()






