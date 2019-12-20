my_list = ['crazy_it', 20, 'Python']  # 使用方括号定义列表，各个成员能赋值
print(my_list)  # ['crazy_it', 20, 'Python']
my_tuple = ('crazy_it', 20, 'Python')  # 使用圆括号定义元组，不能对成员赋值，成员都为const
print(my_tuple)  # ('crazy_it', 20, 'Python')

print(my_tuple[0])  # crazy_it 访问元组第一个元素
print(my_tuple[1])  # 20 访问元组第二个元素
print(my_tuple[-1])  # Python 访问元组倒数第一个元素

a_tuple = ('crazy_it', 20, 5.6, 'f_kit', -17)
print(a_tuple[1:3])  # (20, 5.6) 访问第2个到第4个（不包含）的所有元素
print(a_tuple[-3:-1])  # (5.6, 'f_kit') 访问倒数第3个到倒数第一个（不包含）的所有元素
print(a_tuple[:-3])  # ('crazy_it', 20) 访问开始到倒数第三个（不包含）的所有元素
print(a_tuple[2:])  # (5.6, 'f_kit', -17) 访问第二个到最后一个的所有元素

b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(b_tuple[2:8:2])  # (3, 5, 7) 访问第3个到第9个（不包含）、间隔为2的所有元素
print(b_tuple[2:8:3])  # (3, 6) 访问第3个到第9个（不包含）、间隔为3的所有元素
print(b_tuple[2:-2:2])  # (3, 5, 7) 访问第3个到倒数第二个（不包含）、间隔为2的所有元素

sum_tuple = a_tuple + b_tuple  # ('crazy_it', 20, 5.6, 'f_kit', -17, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(sum_tuple)

mul_tuple = b_tuple * 2
print(mul_tuple)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9)

order_endings = (('st', 'nd', 'rd') + ('th',) * 7) * 3 + ('st',)  # 只有一个元素的元组/列表，需要加','以区分
print(len(order_endings))  # len
day = input("请输入日期：")
day_int = int(day)
if day_int <= 31:
    print(day + order_endings[day_int - 1])  # 只支持字符串加发连接，如使用day_int会报错
    print(day_int, order_endings[day_int - 1], sep="")  # 可以使用','进行连接，默认连接符是' '
else:
    print('日期超过范围')

print(20 in a_tuple)  # True
print(1.2 not in a_tuple)  # True

c_tuple = (20, 10, -2, 15.2, 102, 50)
print(max(c_tuple))  # 102
print(min(c_tuple))  # -2
print(len(c_tuple))  # 6
d_tuple = ('crazy_it', 'f_kit', 'Python', 'Kotlin')
print(max(d_tuple))  # 字符串按ASCII码比较，从第一个字符开始排序
print(min(d_tuple))
print(len(d_tuple))
e_tuple = c_tuple + d_tuple  # int/float序列和str序列
print(e_tuple)
print(type(e_tuple[0]))  # <class 'int'>
print(type(e_tuple[6]))  # <class 'str'>
