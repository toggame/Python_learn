import cmath  # 导入cmath模块

ac1 = 3 + 0.2j
print(ac1)
print(type(ac1))
ac2 = 4 - 0.1j
print(ac2)
# 复数运算
print(ac1 + ac2)  # 输出7+0.1j
# sqrt()是cmath模块下的函数，用于计算平方根
ac3 = cmath.sqrt(-1)
print(ac3)
