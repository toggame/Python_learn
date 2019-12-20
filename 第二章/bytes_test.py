# 创建一个空的bytes
b1 = bytes()
# 创建一个空的bytes值
b2 = b''
# 通过b浅醉指定hello是bytes类型的值
b3 = b'hello'
print(b3)
print(b3[0])
print(b3[2:4])  # 输出ll，后续了解？？？？
# 调用bytes方法将字符串转化为bytes对象
b4 = bytes('我爱Python编程', encoding='utf-8')
print(b4)
# 利用字符串的encode()方法编码成bytes，默认使用UTF-8字符集
b5 = "学习Python很有趣".encode()
print(b5)
# 将bytes对象解码成字符串，默认使用UTF-8进行解码
st = b5.decode()
print(st)  # 学习Python很有趣
b6 = bytes('学', encoding='utf-8')
print(b6)
