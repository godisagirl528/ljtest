"""
    1. driver获取 class(), 打开浏览器 并且获得driver
    2. 常用方法封装好
        - 查找元素
        - 点击
        - 输入

    效果：可以自定义添加selenium的方法 a.获取原始的driver来操作： b.将这个方法封装到这个类里面
        - 我们的类就可以重复使用
    
    掌握：封装原理，怎么进行封装的；不过瘾，可以实现自己实现一遍。
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class PySelenium():

    def __init__(self, browser="chrome", url=None, exe_driver="chromedriver.exe"):
        """
            初始化driver，并且打开浏览器
        """
        browser = browser.lower() # 把所有大写的字符变成小写的字符串

        # 判断为谷歌浏览器/火狐/ie/edge
        if browser == "chrome" or browser == "ch":
            self._driver = webdriver.Chrome(executable_path=exe_driver)
        if browser == "firefox" or browser == "ff":
            self._driver = webdriver.Firefox(executable_path=exe_driver)
        if browser == "internet explorer" or browser == "ie":
            self._driver = webdriver.Ie(executable_path=exe_driver)
        if browser == "edge" or browser == "ed":
            self._driver = webdriver.Edge(executable_path=exe_driver)
        
        try:
            self._driver.get(url)
        except:
            raise Exception("打开浏览器失败！")

    def get_origin_driver(self):
        """
            获取webdriver初始化driver
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

    # 点击方法：只传入locator,就让元素自动点击
    def click(self, locator):
        """
            单击左键
            - locator
        """
        element = self.find_element(*locator)
        element.click()

    def switch_to_frame(self, locator):
        """
            切换到frame
        """
        element = self.find_element(*locator)
        self._driver.switch_to_frame(element)

    def switch_to_default_content(self):
        """
            切换到默认的作用域
        """
        self._driver.switch_to_default_content()

    def quit(self):
        """
            退出driver
        """
        self._driver.quit()

    def close(self):
        """
            关闭浏览器
        """
        self._driver.close()

    def wait(self, timeout=10):
        """
            动态等待方法
        """
        self._driver.implicitly_wait(timeout)


if __name__ == "__main__":
    driver = PySelenium(url="https://www.baidu.com/")
    
    locator = ("id", "kw")
    driver.find_element(locator=locator).send_keys("浪晋小课堂")