a = int(input('请输入整数a：'))
b = int(input('请输入整数b：'))
print(a // b)
print(a / b)
print(a + b)
print(a - b)
print(a * b)

st1 = input('请输入字符串：')
st2 = input('请输入子串：')
ct = 0
print(st1.count(st2))  # count计数不会重复
for i in range(len(st1)):  # range默认0 start，不包含end项
    if st1[i: i + len(st2)] == st2:
        ct += 1
print(ct)

print('二进制：%s' % bin(a))
print('十六进制：%s' % hex(a))  # 会带出0x
print('十六进制：%x' % a)  # 不会带出0x，可自行在文本中添加
