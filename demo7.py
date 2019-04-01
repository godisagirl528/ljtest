from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver")
driver.get("http://www.baidu.com")
ele = driver.find_elements_by_id("kw")
print(ele)
print(type(ele))
print(len(ele))
driver.quit()