from selenium import webdriver
import time

def get_element(driver,byvalue):
    '''
    driver就是实例化的浏览器方法。
    get_element(driver,"id->kw")
    '''
    by = byvalue.split('->')[0]
    value = byvalue.split('->')[1]
    if by == "name":
        ele = driver.find_element_by_name(value)  # name定位到搜索框并输入搜索的内容
    elif by == "id":
        ele = driver.find_element_by_id(value)  # id定位到搜索框并输入搜索的内容
    elif by == "xpath":
        ele = driver.find_element_by_xpath(value)  # xpath定位到搜索框并输入搜索的内容
    elif by == "css":
        ele = driver.find_element_by_css_selector(value)  # css_selector
    elif by == "class":
        ele = driver.find_element_by_class_name(value)   # class name
    elif by == "tag":
        ele = driver.find_element_by_tag_name(value)   # tag_name 
    elif by == "link":
        ele = driver.find_element_by_link_text(value)   # link_text
    elif by == "partial":
        ele = driver.find_element_by_partial_link_text(value)   # partial_link_text
    else:
        print("定位方式不存在，请检查输入的值！！！")
        
    return ele


def send_content(driver,byvalue,content):
    '''
    定位和输入的动作写在一起了。
    '''
    ele = get_element(driver,byvalue)
    ele.send_keys(content)



driver = webdriver.Chrome(executable_path="chromedriver")   # 浏览器的初始化
time.sleep(5)
driver.get("http://www.baidu.com")   # 通过浏览器访问对应的地址
time.sleep(2)
send_content(driver,"class->s_ipt","浪晋的测试小讲堂")
time.sleep(4)
get_element(driver,"id->su").click()  # 定位到百度一下按钮，并点击
time.sleep(5)
driver.quit()   # 关闭浏览器
