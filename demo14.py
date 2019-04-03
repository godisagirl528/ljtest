from appium import webdriver

# # 1. 准备连接手机的资料
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '5.1.1' # 改我
# desired_caps['deviceName'] = 'vivo x6plus'    # 改我
# desired_caps['appPackage'] = "io.appium.android.apis" # 被测app的包名，每一个app都有独立的包名字
# desired_caps['appActivity'] = '.ApiDemos'
# desired_caps['unicodeKeyboard']=True
# desired_caps['resetKeyboard']=True

# # 2. 启动app
# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# # 3. 查找app的元素，来进行操作
# element = driver.find_element_by_id("android:id/text1")
# element.click()

# # 4. 断言结果
# element = driver.find_element_by_xpath("//android.widget.TextView[@text='Accessibility Node Provider' and @content-desc='Accessibility Node Provider']")
# assert element is not None
# print("执行通过了!")

def get_driver():
    """
    
    """
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1' # 改我
    desired_caps['deviceName'] = 'vivo x6plus'    # 改我
    desired_caps['appPackage'] = "io.appium.android.apis" # 被测app的包名，每一个app都有独立的包名字
    desired_caps['appActivity'] = '.ApiDemos'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # 一旦执行这句话后，appium会自动启动app
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    return driver



def test_01():
    driver = get_driver()

    # element = driver.find_element_by_accessibility_id("App") # 文本查找
    # element.click()

    # element = driver.find_element_by_id("android:id/text1") # resource-id查找
    element = driver.find_element_by_accessibility_id("Accessibility") # 文本查找
    element.click()
    # driver.find_element_by_xpath("//android.widget.TextView[@text='Accessibility Node Provider' and @content-desc='Accessibility Node Provider']") # xpath查找
    # driver.find_element_by_android_uiautomator('new UiSelector().text("Accessibility Node Querying")') # 外单内双 content-desc查找

    print("执行通过了!")

def test_02():
    driver = get_driver()

    element = driver.find_element_by_accessibility_id("App")
    element.click()

    element = driver.find_element_by_accessibility_id("Search")
    element.click()

    element = driver.find_element_by_accessibility_id("Invoke Search")
    element.click()

    xpath = "//android.widget.EditText[@resource-id='io.appium.android.apis:id/txt_query_prefill']"
    element = driver.find_element_by_xpath(xpath)

    # 1. send_keys方式输入：很慢
    # element.send_keys("123")

    # set_value:很快
    driver.set_value(element, "ljtest")

    # 返回
    # driver.back()


if __name__ == "__main__":
    test_02()