a_tuple = ('crazy_it', 20, -1.2)
a_list = list(a_tuple)  # ('crazy_it', 20, -1.2) ['crazy_it', 20, -1.2] 将元组转化为列表
print(a_tuple, a_list)

a_range = range(1, 5)
print(a_range)  # range(1, 5)
b_list = list(a_range)  # [1, 2, 3, 4] 将范围转化为列表
print(b_list)
c_list = list(range(4, 20, 3))
print(c_list)  # [4, 7, 10, 13, 16, 19]

a_tuple = tuple(a_list)
print(a_tuple)  # ('crazy_it', 20, -1.2) 将列表转化为元组
b_tuple = tuple(a_range)
print(b_tuple)  # (1, 2, 3, 4)
c_tuple = tuple(range(4, 20, 3))  # 将范围转化为元组
print(c_tuple)  # (4, 7, 10, 13, 16, 19)

a_list.append('f_kit')
print(a_list)  # ['crazy_it', 20, -1.2, 'f_kit']
a_list.append(a_tuple)
print(a_list)  # ['crazy_it', 20, -1.2, 'f_kit', ('crazy_it', 20, -1.2)] a_tuple元组当成一个元素加入a_list
a_list.append(['a', 'b'])
print(a_list)  # ['crazy_it', 20, -1.2, 'f_kit', ('crazy_it', 20, -1.2), ['a', 'b']] 列表当成一个元素加入a_list

b_list = ['a', 30]
b_list.extend((-2, 3.1))
print(b_list)  # ['a', 30, -2, 3.1] 追加元组中的所有元素
b_list.extend(['C', 'R', 'A'])
print(b_list)  # ['a', 30, -2, 3.1, 'C', 'R', 'A'] 追加列表中的所有元素
b_list.extend(range(97, 100))
print(b_list)  # ['a', 30, -2, 3.1, 'C', 'R', 'A', 97, 98, 99] 追加区间中的所有元素

c_list = list(range(1, 6))
print(c_list)  # [1, 2, 3, 4, 5]
c_list.insert(3, 'crazy_it')
print(c_list)  # [1, 2, 3, 'crazy_it', 4, 5]  在索引3处插入字符串
c_list.insert(3, tuple('crazy'))
print(c_list)  # [1, 2, 3, ('c', 'r', 'a', 'z', 'y'), 'crazy_it', 4, 5] 在索引3增加元组
c_list.insert(3, list('crazy'))
print(c_list)  # [1, 2, 3, ['c', 'r', 'a', 'z', 'y'], ('c', 'r', 'a', 'z', 'y'), 'crazy_it', 4, 5] 在索引3处增加列表

a_list = ['crazy_it', 20, -2.4, (3, 4), 'f_kit']
del a_list[2]
print(a_list)  # ['crazy_it', 20, (3, 4), 'f_kit'] 删除第3个元素
del a_list[1:3]
print(a_list)  # ['crazy_it', 'f_kit'] 删除第2到第4（不包含）个元素,slice法
b_list = list(range(1, 10))
del b_list[2:-2:2]
print(b_list)  # 删除第3个到倒数第2个（不包含）元素，间隔为2，slice法

name = 'crazy_it'
print(name)  # crazy_it
del name
# print(name)  # NameError

c_list = [20, 'crazy_it', 30, -4, 'crazy_it', 3.4]
c_list.remove(30)
print(c_list)  # [20, 'crazy_it', -4, 'crazy_it', 3.4] 删除第一个找到的30
c_list.remove('crazy_it')
print(c_list)  # [20, -4, 'crazy_it', 3.4] 删除第一个找到的'crazy_it'

c_list = [20, 'crazy_it', 30, -4, 'crazy_it', 3.4]  # 删除所有'crazy_it'
i = 0
kw_remove = 'crazy_it'
for i in range(len(c_list)):
    if kw_remove in c_list:
        c_list.remove(kw_remove)
        i += 1
    else:
        break
print(c_list)  # [20, 30, -4, 3.4]

c_list.clear()
print(c_list)  # [] 清除所有元素

a_list = [2, 4, -3.4, 'crazy_it', 23]
a_list[2] = 'f_kit'
print(a_list)  # [2, 4, 'f_kit', 'crazy_it', 23] 列表可以对元素进行赋值，但元组不可以
a_list[-2] = 9527
print(a_list)  # [2, 4, 'f_kit', 9527, 23]

b_list = list(range(1, 5))
print(b_list)  # [1, 2, 3, 4]
b_list[1:3] = ['a', 'b']
print(b_list)  # [1, 'a', 'b', 4] 将第2和第3个元素更换为'a','b'
b_list[1:4] = ['a', 'b']
print(b_list)  # [1, 'a', 'b'] 赋值列表中仅有2个元素，为此b_list中的第4个元素将被删除
b_list[1:3] = ['a', 'b', 'c', 'd']
print(b_list)  # [1, 'a', 'b', 'c', 'd'] 当赋值列表中多于赋值序列，将会从start索引处开始进行覆盖
b_list[2:2] = ['x', 'y']
print(b_list)  # [1, 'a', 'x', 'y', 'b', 'c', 'd'] 当赋值序列为空时，等同于从start索引处开始插入元素
b_list[2:5] = []
print(b_list)  # [1, 'a', 'c', 'd'] 当赋值为空时，等同于删除列表元素
b_list[1:3] = 'Charlie'
print(b_list)  # [1, 'C', 'h', 'a', 'r', 'l', 'i', 'e', 'd'] 当使用slice语法赋值单个字符串，会将字符串自动转化为序列
# b_list[1:3] = 2  # TypeError 无法使用slice语法赋值单个数值

c_list = list(range(1, 10))
c_list[2:9:2] = ['a', 'b', 'c', 'd']
print(c_list)  # [1, 2, 'a', 4, 'b', 6, 'c', 8, 'd']
# c_list[2:9:2] = ['a', 'b']  # ValueError 使用step时，赋值列表元素与所替换的列表元素个数必须相等

a_list = [2, 30, 'a', [5, 30], 30, 30.0, 0x1e]
print(a_list.count(30))  # 4 count统计列表中某个元素出现的次数，列表中的嵌套列表会作为一个整体参与计数
print(a_list.count(30.0))  # 4 count对于浮点、不同进制的整型会自动进行转化
print(a_list.count('30'))  # 0 严格区分数值类型
print(a_list.count([5, 30]))  # 1

a_list = [2, 30, 'a', 'b', 'crazy_it', 30]
print(a_list.index(30))  # 1 定位30第一次出现的索引号
print(a_list.index(30, 2))  # 5 从索引2开始，定位30第一次出现的索引号
# print(a_list.index(30, 2, 4))  # ValueError: 30 is not in list
# index(self,object: _T,start: int = ...,stop: int = ...) -> int

stack = list()
stack.append('f_kit')
stack.append('crazy_it')
stack.append('Charlie')
print(stack.pop())  # Charlie  pop会返回相应的出栈元素
# pop(self, index: int = ...) -> _T 默认index为last，功能类似与del list(-1)，但del不会返回移除的元素
print(stack)  # ['f_kit', 'crazy_it']
print(stack.pop(1))  # crazy_it 可按索引进行出栈
print(stack)  # ['f_kit']
# stack.extend(['crazy_it', 'Charlie'])
# print(stack)
# print(stack.pop[-2:-1])  # TypeError: 'builtin_function_or_method' object is not subscriptable pop不支持slice
stack.append([1, 2])
print(stack.pop())  # [1, 2] 嵌套列表和元组也会作为一个整体出栈
print(stack)  # ['f_kit']

a_list = list(range(1, 8))
a_list.reverse()
print(a_list)  # [7, 6, 5, 4, 3, 2, 1] 将元素全部反转
print(a_list.reverse())  # None reverse不会返回值

a_list = [3, 4, -2, -30, 14, 9.3, 3.4]
a_list.sort()
# sort(self, *, key: Optional[(_T) -> Any] = ..., reverse: bool = ...) -> None 默认升序，reverse可改为降序。相同的值会维持原顺序
print(a_list)  # [-30, -2, 3, 3.4, 4, 9.3, 14]
a_list.sort(reverse=True)
print(a_list)  # [14, 9.3, 4, 3.4, 3, -2, -30]
b_list = ['Python', 'Swift', 'Ruby', 'Go', 'Kotlin', 'Erl']
b_list.sort()
print(b_list)  # ['Erl', 'Go', 'Kotlin', 'Python', 'Ruby', 'Swift'] 字符串一次对比各个字符的编码大小
b_list.sort(key=len)  # 关键字参数  按字符串的长度排序
print(b_list)  # ['Go', 'Erl', 'Ruby', 'Swift', 'Kotlin', 'Python']
b_list.sort(key=len, reverse=True)
print(b_list)  # ['Kotlin', 'Python', 'Swift', 'Ruby', 'Erl', 'Go']  相同的值会维持原顺序
