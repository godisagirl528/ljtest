import pymysql
import requests
from demo12 import read_excel


def test_01():
    """
        get方法:获取资源用的
    """
    url = "http://118.24.29.59:5000/"
    response = requests.get(url=url)
    
    # .text获取响应的文本
    # print(response.text)
    # 获取响应http状态码
    # print(response.status_code)

    # post方法：传参用的
    
    
def test_02():
    """
        post方法
    """

    # 传Json格式
    # url = "http://118.24.29.59:5000/userRegist/"
    # data = {"username":"user3322", "password":"123", "nickname":"user33"}
    # response = requests.post(url=url, json=data)

    # print(response.text)
    # # 获取相应文本的json格式, dict
    # result = response.json()
    # print(result.get("code"))
    # print(result.get("data"))

    # 传form-data格式，postman生成代码
    url = "http://118.24.29.59:8080/morning/user/userLogin"
    querystring = {"user.loginName":"2941635995@qq.com","user.loginPassword":"a123456"}
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"useranme\"\r\n\r\npassword\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'Postman-Token': "9ed34daa-7e86-44b0-beff-74d249e122f3"
        }
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)


def request(method="GET", url=None, data={}, headers={}, json={}):
    """
        request二次封装
    """
    return requests.request(method=method, url=url, data=data, headers=headers, json=json)


def test_03():
    """
        接口测试demo
    """
    # 1. 构造请求
    url = "http://118.24.29.59:5000/userRegist/"
    data = {"username":"ljtest", "password":"ljtest", "nickname":"user33"}
    response = request(method="post", url=url, json=data)
    # 2. 判断http响应状态码:断言
    # 断言：如果断言通过，程序继续执行；反之，抛出异常，程序终止
    assert response.status_code == 200
    # 3. 判断接口响应数据
    res = response.json() # 此时就是一个字典
    assert res.get("code") == 200
    # 4. 查询数据库，查找是否存在此数据：验证程序是否存在问题
    sql = "select * from tbl_user where username='{}'".format(data.get("username"))
    db_info = ("118.24.29.59","root","123456","lux")
    res = _query(sql=sql, db_info=db_info)
    assert len(res) != 0

    print("测试用例执行成功！！！")


def test_04():
    """
        数据驱动Demo
    """
    sheet_name = "Sheet1"
    excel_path = "接口测试用例模板.xlsx"
    results = read_excel(excel_path, sheet_name)

    for case in results:
        # 取需要的数据
        print("-------------------------------")
        url = case[1]                   # url
        method = case[5]                # http方法
        data = eval(case[7])            # data数据
        expect_http_code = case[8]      # http状态码
        expect_response_code = case[9]  # code

        response = request(method=method, url=url, json=data)
        try:
            assert expect_http_code == response.status_code
            assert expect_response_code == response.json().get("code")
            # 查询数据库，查看是否存在这个用户
            username = data.get("username")
            password = data.get("password")
            sql = "select * from tbl_user where username='{}' and password='{}'".format(username, password)
            db_info = ("118.24.29.59","root","123456","lux")
            res = _query(sql=sql, db_info=db_info)
            assert len(res) != 0
            print("用例执行成功！")
        except:
            print(response.json())
            print("用例执行失败了！")


def _query(sql, db_info):
    '''
    通过sql查询数据库的值，并返回
    '''
    db = pymysql.connect(*db_info)  # 连接数据库
    cursor = db.cursor()   # 获取游标
    cursor.execute(sql)   # 执行SQL
    res = cursor.fetchall()   # 获取查询到的值
    db.close()   # 关闭数据库连接
    return res


if __name__ == "__main__":
    # test_01()
    # test_02()
    # url = "http://118.24.29.59:5000/"
    # print(request(method="GET", url=url).text)
    
    # url = "http://118.24.29.59:5000/userRegist/"
    # data = {"username":"user3322", "password":"123", "nickname":"user33"}
    # print(request(method="POST",url=url, json=data).text)

    # test_03()
    test_04()