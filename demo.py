'''
现在我们有一个班的同学的成绩，以数组形式体现出来。
[88,98,67,54,65,54,98,34,56,78,46,77,33,44,55,66]
现在我们要把80分以上的成绩单独的存放，80分以下的单独的存放成两个不同的数组。
并且输出两个数组。
'''
# htuple = ()  # 元组，只读，不可修改，操作方式和数据一样
# hlist = [123,"王二",23,"女"]  # 数组
# hdict = {}  # 字典

'''
今天是2019年的3月25日，
请通过编程的手段来确认今天是今年的第几天。
'''
def shijian():
    today = input("请按此格式输入今天的日期（2019-3-25）：")
    todaylist = today.split("-")
    year = int(todaylist[0])
    month = int(todaylist[1])
    day = int(todaylist[2])
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



def chengfa(a,b):
    '''
    用法：chengfa(1,2)
    说明：传入两个数字，返回乘积。
    '''
    return a*b
