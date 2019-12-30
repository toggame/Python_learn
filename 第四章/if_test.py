s_age = input('请输入您的年龄：')
age = int(s_age)
if age > 20:
    print('您的年龄已经大于20岁了')
    print('20岁以上的人应该学会承担责任..')  # 缩进的多行代码作为代码块，成为完整的条件执行体
else:
    print('1')

s = ''
if s:
    print('s不是空字符')
else:
    print('s是空字符')  # 空字符会作为false

my_list = []
if my_list:
    print('my_list不是空字符')
else:
    print('my_list是空列表')  # 空列表会作为false

my_tuple = ()
if my_tuple:
    print('my_tuple不是空元组')
else:
    print('my_tuple是空元组')  # 空元组会作为false

if age > 60:
    print('老年人')
elif age > 40:
    print('中年人')  # elif及else存在隐含条件，即对之前的条件取反
elif age > 20:
    print('青年人')

s = int(input('请输入一个整数：'))
if s > 5:
    print('大于5')
elif s < 5:
    pass  # 使用pass作为空语句，不执行
else:
    print('等于5')

assert 20 < age < 80  # 当结果为False时，会报AssertionError错误
assert True + False  # 类似if，可用计算值和逻辑值
