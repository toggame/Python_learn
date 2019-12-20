s1 = '这本书的价格是：'
p = 99.8
# 字符串直接拼接数值，程序报错
# print(s1 + p)
print(s1 + str(p))
print(s1 + repr(p))
st = "I will play my fife"
print(st)
print(str(st))
print(repr(st))  # repr会输出Python表达式形式，原格式如果是文本，则会带上引号,转义符也会输出原格式
st1 = '"we ar scared, Let\'s hide in the shade'
print(repr(st1))
print(str(st1))
