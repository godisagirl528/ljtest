import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

"""
    记住有哪些功能，不会用的时候再来查用法
"""

def mouse_event():
    """
        鼠标事件
        - 单击
        - 双击
        - 移动
        - 右键
    """
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.get("https://www.baidu.com")

    # 将鼠标移动到设置上面
    element = driver.find_element_by_link_text("设置")
    ActionChains(driver).move_to_element(element).perform() # 将鼠标移动到设置元素上面

    # 单击
    # element.click()

    # 右键
    # element = driver.find_element_by_link_text("新闻")
    # ActionChains(driver).context_click(element).perform() # 右键

    # 双击：点两次左键
    # element = driver.find_element_by_link_text("新闻")
    # ActionChains(driver).double_click(element).perform()

    time.sleep(3)


def keyboard_event():

    """
        键盘事件：按键，回车/空格/删除
    """
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.get("https://www.baidu.com")
    search = driver.find_element_by_id("kw")
    search.send_keys("pythone")
    time.sleep(3)

    # 删除掉搜索框的内容，再输入
    # search.clear()
    # search.send_keys("python")

    # 点一下向左边删除按键
    # search.send_keys(Keys.BACK_SPACE)

    # 按一下刷新键
    # search.send_keys(Keys.F5)

    # 返回页面事件
    driver.back()
    time.sleep(3)
    # 前进页面事件
    driver.forward()

    time.sleep(3)
    driver.quit()

    # 删除多余的字符

# iframe，网页嵌套网页
# 把driver作用域切换到iframe，再查找元素
# 如果执行完了之后，需要切换到默认的作用域里面
def iframe():
    """
        切换为页面frame的例子
    """
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.get("https://passport2.eastmoney.com/pub/login")

    # 先查找iframe，再切换到iframe作用域，最后再来查找登录
    frame = driver.find_element_by_id("frame_login")
    driver.switch_to_frame(frame)
    driver.find_element_by_id("txt_account").send_keys("13000000000")

    time.sleep(3)
    # 如果执行完了之后，需要切换到默认的作用域里面，再查找默认域的元素
    driver.switch_to_default_content()
    driver.find_element_by_link_text("点此进入基金交易").click()
    time.sleep(3)


if __name__ == "__main__":
    # mouse_event()
    # keyboard_event()
    iframe()