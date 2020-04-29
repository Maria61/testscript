from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

t = driver.title
print(t)
url = driver.current_url
print(url)

# driver.find_element_by_id("kw").send_keys("赵丽颖")
# driver.find_element_by_id("su").click()
# # time.sleep(6) #固定时间等待
# # driver.implicitly_wait(10) #智能时间等待
# driver.find_element_by_link_text("赵丽颖_百度百科").click()

# time.sleep(6)
driver.quit()