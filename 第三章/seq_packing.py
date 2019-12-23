val = 10, 20, 30  # 序列封包，将10、20、30封装成元组后赋值给val
print(val)  # (10, 20, 30) 多个赋值的结果是元组
val = 20, 30, 40
print(val)  # (20, 30, 40) 多个赋值的结果是元组，可以重新赋值，元组也会变更，但无法变更其中某一元素
print(type(val))  # <class 'tuple'>
print(val[0])  # 20

a_tuple = tuple(range(1, 10, 2))
print(a_tuple)  # (1, 3, 5, 7, 9)
a_list = list(range(1, 10, 2))
print(a_list)  # [1, 3, 5, 7, 9]

a, b, c, d, e = a_tuple  # 序列解包：将a_tuple元组的各元素一次赋值给a、b、c、d、e
print(a, b, c, d, e)  # 1 3 5 7 9
a_list = ['f_kit', 'crazy_it']
a_str, b_str = a_list  # 序列解包
print(a_str, b_str)  # f_kit crazy_it

x, y, z = 10, 20, 30  # 依次赋值给x、y、z，实际上是先对10、20、30封装为一个元组后再解包赋值给x、y、z
print(x, y, z)  # 10 20 30
x, y, z = y, z, x  # 可实现交换变量的值
print(x, y, z)  # 20 30 10

first, second, *rest = range(10)  # 部分解包，first,second对应第一和第二元素，其余的都存在列表rest中
print(first, second)  # 1 2
print(rest)  # [3, 4, 5, 6, 7, 8, 9]

*begin, last = range(10)
print(begin, last)  # [0, 1, 2, 3, 4, 5, 6, 7, 8] 9
first, *middle, last = range(10)
print(first, middle, last)  # 0 [1, 2, 3, 4, 5, 6, 7, 8] 9
