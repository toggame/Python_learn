print(not False)  # True
print(5 > 3 and 20.0 > 10)  # True
print(5 > 3 and 20.0 > 10)  # True
print(4 > 5 or "c" > "a")  # True

bookName = '学习Python'
price = 79
version = '正式版'
if bookName.endswith('Python') and (price < 50 or version == '正式版'):
    print('打算购买')
else:
    print('不购买')

a = 5
b = 8
st = "a大于b" if a > b else "a不大于b"
print(st)
print("a大于b") if a > b else print("a不大于b")
c = 5
print('c大于a') if c > a else print('c小于a') if c < a else print('c等于a')

s = 'crazyit.org'
print('it' in s)
print('it' not in s)
print('fff' in s)
print('fff' not in s)
