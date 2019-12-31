count_i = 0  # 循环的初始化条件
while count_i < 10:  # 当count_i 小于10时，执行循环体
    print('count:', count_i)  # 循环体
    count_i += 1  # 循环迭代语句
print('循环结束')

# count_i2 = 0
# while count_i2 < 10:
#     print('不停执行的死循环:', count_i2)
#     count_i2 -= 1
# print('永远无法跳出的循环体')

a_tuple = ('fkit', 'crazyit', 'Charlie')
i = 0
while i < len(a_tuple):
    print(a_tuple[i])  # 可作为索引进行遍历
    i += 1

src_list = [12, 45, 34, 13, 100, 24, 56, 74, 109, '123', 1.2, 1 + 1j]
a_list = []  # 被3整除的元素
b_list = []  # 被3除余1的元素
c_list = []  # 被3除余2的元素
d_list = []  # 非整型的元素
while len(src_list) > 0:  # 将scr_list的元素数作为循环条件
    ele = src_list.pop()  # 出栈元素并赋值
    if type(ele) == int:  # 防止非整型元素报错
        if ele % 3 == 0:
            a_list.append(ele)
        elif ele % 3 == 1:
            b_list.append(ele)
        else:
            c_list.append(ele)
    else:
        d_list.append(ele)
a_list.sort()
b_list.sort()
c_list.sort()
print('被3整除的元素：', a_list)
print('被3除余1的元素：', b_list)
print('被3除余2的元素：', c_list)
print('非整型的元素', d_list)

count_i = 0
while count_i < 5:
    print('count_i小于5：', count_i)
    count_i += 1
else:  # 当跳出while时会执行else的代码块，结果与将代码块防止while循环体外结果相同，但可以增加代码可读性。其他语言通常不支持
    print('count_i大于等于5：', count_i)  # count_i的值等于跳出while循环体时的值
print('循环体外:', count_i)
