a_range = range(10)
a_list = [x * x for x in a_range]  # 以输出0~9的平方列表，
print(a_list)

b_list = [x * x for x in a_range if x % 2 == 0]  # for表达式可以接if表达式，仅满足要求的添加仅列表元素
print(b_list)

c_generator = (x * x for x in a_range if x % 2 == 0)
print(type(c_generator))  # <class 'generator'> for表达时如果使用圆括号，生成的是生成器而不是元组
print(c_generator)  # <generator object <genexpr> at 0x000002262DF26430> 生成器无法直接print
for i in c_generator:  # 生成器可用于for循环迭代
    print(i, end='\t')
print()
c_dict = dict.fromkeys(c_generator)
print(c_dict)  # {}  生成器不能用于生成字典
c_dict = dict.fromkeys(b_list)
print(c_dict)  # {0: None, 4: None, 16: None, 36: None, 64: None}

d_list = [(x, y) for x in range(3) for y in range(2)]  # 后面的for表达式作为前面的for表达式的嵌套
print(d_list)  # [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
dd_list = []
for x in range(3):  # 等效该方法
    for y in range(2):
        dd_list.append((x, y))
print(dd_list)

src_a = [30, 12, 66, 34, 39, 78, 36, 57, 121]
src_b = [3, 5, 7, 11]
e_list = [(x, y) for x in src_a for y in src_b if x % y == 0]
print(e_list)
