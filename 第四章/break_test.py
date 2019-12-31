for i in range(10):
    print('i的值为：', i)
    if i == 2:
        break  # 当i=2时，跳出循环
# i的值为： 0
# i的值为： 1
# i的值为： 2
###############################
for i in range(10):
    print('i的值为：', i)
    if i == 2:
        break
    else:
        print('else块：', i)  # 该语句在i == 2时不会执行
# i的值为： 0
# else块： 0
# i的值为： 1
# else块： 1
# i的值为： 2
###############################

my_list = []
for i in range(3):
    for j in range(3):
        my_list.append((i, j))
        if j == 1:
            break  # 仅会跳出本级循环
print(my_list)  # [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
###############################

exit_flag = False
for i in range(5):
    for j in range(3):
        print('i的值为：%d，j的值为：%d' % (i, j))
        if j == 1:
            exit_flag = True
            break
    if exit_flag:
        break  # 因Python的break不支持标签，如需跳出多级循环，需要定义标志来
# i的值为：0，j的值为：0
# i的值为：0，j的值为：1
###############################

for i in range(3):
    print('i的值是：', i)
    if i == 1:
        continue  # 忽略当前循环的后续语句
    print('continue后的输出语句')  # 当i == 1时，不执行该语句


# i的值是： 0
# continue后的输出语句
# i的值是： 1
# i的值是： 2
# continue后的输出语句
###############################

def test():
    for x in range(10):
        for y in range(10):
            print('x的值是：%d，y的值是：%d' % (x, y))
            if y == 1:
                return 1  # 跳出该函数、方法，并返回相应的的值
            print('return后的输出语句')


test()
print(test())
# x的值是：0，y的值是：0
# return后的输出语句
# x的值是：0，y的值是：1
# x的值是：0，y的值是：0
# return后的输出语句
# x的值是：0，y的值是：1
# 1
###############################
