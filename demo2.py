


def gettoday(today):
    '''
    请按此格式输入今天的日期（2019-3-25）
    '''
# today = input("请按此格式输入今天的日期（2019-3-25）：")
    todaylist = today.split("-")
    try:
        year = int(todaylist[0])
        month = int(todaylist[1])
        day = int(todaylist[2])
    except:
        print("输入的格式不正确，异常退出！！")
        exit()
    if month > 12:
        print("请输入正确的月份！！！")
        exit()
    monthlist = [31,28,31,30,31,30,31,31,30,31,30,31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        monthlist[1] = 29
    res = 0
    for i in range(month-1):
        res += monthlist[i]
    res = res + day
    print("今天是%d年的第%d天！" % (year, res))





def total(a):
    '''
    说明：用来计算输入的字符串的长度,
    a 就是传入的字符串的变量
    '''
    lang = len(a)
    print('这段话一共有',lang,'个字!!')






def printnum(a):
    '''
    题目：
    定义一个方法，这个方法的功能是输入一个数字，比如5，那么会打印出一个三角形，
    格式如下：
    1
    22
    333
    4444
    55555
    '''
    for i in range(1,a+1):
        print(i*str(i))



'''
@全体成员 
今天的作业1：
http://www.runoob.com/quiz/python-quiz.html
做下简单的选择题。
2、编程练习。
2.1   设计一个方法，这个方法的功能是，输入一个四位数，计算各个位数的和。如1234,输出结果为10。
2.2   设计一个方法，这个方法的功能是，输入账号密码进行登录，登录成功后，可以进行学生信息的添加，将添加的学生信息存到字典里。添加结束后，打印结果。如果账号密码不对，则直接退出程序。
'''