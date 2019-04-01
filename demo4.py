import pymysql


def query(sql):
    '''
    通过sql查询数据库的值，并返回
    '''
    db = pymysql.connect("127.0.0.1","root","","lux")  # 连接数据库
    cursor = db.cursor()   # 获取游标
    cursor.execute(sql)   # 执行SQL
    res = cursor.fetchall()   # 获取查询到的值
    db.close()   # 关闭数据库连接
    return res

def commit(sql):
    db = pymysql.connect("127.0.0.1","root","","lux")  # 连接数据库
    cursor = db.cursor()   # 获取游标
    cursor.execute(sql)   # 执行SQL
    db.commit()   # 应用提交
    db.close()  # 关闭连接
'''
tangtian	1234156
'''
username = input("请输入账号：")
password = input("请输入密码：")

sql = "select * from t_user where username = '%s';" % username
res = query(sql)
print(res)
if len(res) != 0:
    if password == res[0][2]:
        print("登录成功！！！")
        token = input("请输入要新的token：")
        sql = "update t_user set token = '%s' where id = %s;" % (token, res[0][0])
        commit(sql)
        print("修改token成功！！！")

    else:
        print("密码不正确！！")
else:
    print("账号不存在！！！")



