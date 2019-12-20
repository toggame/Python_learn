import time

print("5是否大于4：", 5 > 4)  # True
print('3的4次方是否大于或等于90：', 3 ** 4 >= 90)  # False
print('20是否大于或等于20.0：', 20 >= 20.0)  # True
print('5和5.0是否相等：', 5 == 5.0)  # True
print('5.2%4.1与1.1是否相等：', 5.2 % 4.1 == 1.1)  # False  浮点精度将会影响值的对比
print('1和True是否相等：', 1 == True)  # True 可以用数值1和True/0和False做对比，但是不建议，使用条件或bool与之对比
print('0和False是否相等：', 0 == False)  # True
print(True + False == True)  # True 进行运算后会变成整数
print(type(True + False))  # int
a = time.gmtime()
b = time.localtime()
c = time.gmtime()
print(a)
print(a.tm_zone)
print(b.tm_zone)
print(a == b)
print(a == c)
print(a is c)  # 值相同，但ID不同
print(id(a), id(c))  # 通过ID判断是否相同
#  >
#  >=
#  <
#  <=
#  ==
#  !=
#  is
#  is not
