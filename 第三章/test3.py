import random

a, b, c = input('请输入a：'), input('请输入b：'), input('请输入c：')
tuple1 = (a, b, c)
print(tuple1 * 3)
print(tuple1 + ('fkjava', 'crazyit'))

list1 = list(range(1, 10))
start, end = int(input('请输入start:')), int(input('请输入end:'))
if start > end:
    print('start大于end，请重新输入')
elif end > len(list1) or start > len(list1):
    print('输入大于长度，请重新输入')
else:
    list2 = list1[start:end]
    print(list2)

n = int(input('请输入序列长度n：'))
my_list = []
#
# 获取随机列表
for i in range(n):  # 方法1
    my_list.append(random.random())  # random.random() 获取[0,1)的随机浮点数
print(my_list)
my_list.clear()  # 方法2
for i in range(n):
    my_list[i:i] = [random.random()]  # 必须赋值给列表
print(my_list)
my_list.clear()  # 方法3
my_list = [random.random() for i in range(n)]
print(my_list)
print([random.random() for i in range(n)])
#
# 获取随机奇数
my_list.clear()  # 方法1
for i in range(n):
    my_list.append(random.randint(0, 100) * 2 + 1)  # randint包含start和end的随机整数
print(my_list)
my_list.clear()  # 方法2
for i in range(n):
    my_list[i:i] = [random.randint(0, 100) * 2 + 1]
print(my_list)
my_list.clear()  # 方法3
my_list = [random.randint(0, 100) * 2 + 1 for i in range(n)]
print(my_list)
#
# 获取随机大写字母
my_list.clear()  # 方法1
for i in range(n):
    my_list.append(chr(random.randint(0x41, 0x5a)))
print(my_list)
my_list.clear()  # 方法2
for i in range(n):
    my_list[i:i] = [chr(random.randint(65, 90))]
print(my_list)
my_list.clear()  # 方法3
my_list = [chr(random.randint(65, 90)) for i in range(n)]
print(my_list)
#
# 输入n个字符串，去除重复项后生成一个列表
input_list = []
for i in range(n):
    input_list.append(input('请输入字符串%s：' % (i + 1)))
my_list.clear()  # 方法1
for i in range(len(input_list)):
    if input_list[i] not in my_list:
        my_list.append(input_list[i])
print(my_list)
my_list.clear()  # 方法2
[my_list.append(str1) for str1 in input_list if str1 not in my_list]  # 新建了一个列表，但并未进行赋值。append命令会对源数据进行变更。
print(my_list)
my_list.clear()  # 方法3
my_list = list(dict.fromkeys(input_list).keys())  # 通过字典的keys会自动剔除重复值，以清除重复项
print(my_list)
#
# 输入以空格分割的多个整数，转化为元组元素后输出，并输出hash值
my_tuple = tuple(input('请输入空格分隔的多个整数：').split())
print(my_tuple)
print(hash(my_tuple))
#
# 随机输入n个大写字母，使用dict统计字母的次数
input_list.clear()
for i in range(n):  # 方法1
    input_list.append(input('请输入字符%s：' % (i + 1)))
my_dict = dict([(i, input_list.count(i)) for i in input_list])
print(my_dict)
my_dict.clear()  # 方法2
my_dict = dict.fromkeys(input_list)
for i in my_dict.keys():
    my_dict[i] = input_list.count(i)
print(my_dict)
