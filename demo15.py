
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class PyAppium():

    # 构造方法
    def __init__(self, url="", desired_caps={}):
        """
            构造方法
        """
        self._driver = self._get_driver(url, desired_caps)
        self.timeout = 30

    def _get_driver(self, url="", desired_caps={}):
        """
            获取driver
        """
        if url == "" or not isinstance(desired_caps, dict):
            raise Exception("参数不正确！")

        return webdriver.Remote(url, desired_caps)

    def get_origin_driver(self):
        """
            获取Appium原始driver
        """
        return self._driver

    def find_element(self, locator):
        """
            查找单个元素
                参数：locator=("id", "kw")
                类型：
                ID = "id"
                XPATH = "xpath"
                LINK_TEXT = "link text"
                PARTIAL_LINK_TEXT = "partial link text"
                NAME = "name"
                TAG_NAME = "tag name"
                CLASS_NAME = "class name"
                CSS_SELECTOR = "css selector"
        """
        # 判断locator参数是否是元素
        if not isinstance(locator, tuple):
            raise Exception("输入的数据必须是(by, value)格式！") # 抛出异常，终止执行
        
        # 动态等待10s去找这个元素，如果超过了10S就抛出找不到元素的异常，程序终止
        try:
            element = WebDriverWait(self._driver, 10).until(lambda s: s.find_element(*locator))
            return element
        except:
            raise Exception("未找到元素{}".format(locator))

    def find_elements(self, locator):
        """
            封装find_elements方法
        """
        if not isinstance(locator, tuple):
            raise("locator参数错误，必须传元素类型：loc=('id', 'value')")

        try:
            elements = WebDriverWait(self._driver,self.timeout).until(lambda x: x.find_elements(*locator))
            return elements #[element1, element2,....]
        except:
            return []

    def click(self, locator):
        """
            点击操作
        """
        element = self.find_element(locator)
        element.click()

    def type(self, locator, keys):
        """
            输入操作：默认键盘设置为appium键盘
        """
        element = self.find_element(locator)
        self._driver.set_value(element, keys)

    def wait(self):
        """
            等待
        """
        self._driver.implicitly_wait(self.timeout)

    def close(self):
        """
            关闭app
        """
        self._driver.close_app()

    def quit(self):
        """
            退出执行
        """
        self._driver.quit()

if __name__ == "__main__":
    url = "http://localhost:4723/wd/hub"
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1' # 改我
    desired_caps['deviceName'] = 'vivo x6plus'    # 改我
    desired_caps['appPackage'] = "io.appium.android.apis" # 被测app的包名，每一个app都有独立的包名字
    desired_caps['appActivity'] = '.ApiDemos'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # 获取PyAppium封装类的对象
    appium = PyAppium(url=url, desired_caps=desired_caps)

    # 通过对象来操作
    # locator = ("xpath", "//android.widget.TextView[@text='App' and @content-desc='App']")
    # appium.find_element(locator).click()

    # locator = ("id", "android:id/text1")
    # elements = appium.find_elements(locator)
    # for element in elements:
    #     element.click()
    #     appium.get_origin_driver().back()

    # locator = ("id", "android:id/text1")
    # appium.click(locator)

    app = ("xpath", "//android.widget.TextView[@text='App' and @content-desc='App']")
    app_search = ("xpath", "//android.widget.TextView[@text='Search' and @content-desc='Search']")
    app_search_invoke = ("xpath", "//android.widget.TextView[@resource-id='android:id/text1' and @text='Invoke Search' and @content-desc='Invoke Search']")
    app_data = ("xpath", "//android.widget.EditText[@resource-id='io.appium.android.apis:id/txt_query_appdata']")

    appium.click(app)
    appium.click(app_search)
    appium.click(app_search_invoke)
    appium.type(app_data, "hello appium!")
