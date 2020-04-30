from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 浏览器的前进与后退与滚动条

# driver.find_element_by_link_text("新闻").click()
# time.sleep(6)
# print(driver.title)
# 后退到前一个页面
# driver.back()
# time.sleep(6)
# print(driver.title)
# 前进到下一个页面
# driver.forward()
# print(driver.title)

driver.find_element_by_id("kw").send_keys("Ella")
driver.find_element_by_id("su").click()
time.sleep(4)

# 让浏览器滑动到最低端
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(4)
# 让浏览器滑动到最顶端
js = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js)

time.sleep(6)
driver.quit()