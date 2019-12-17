s = 'Hello\nCharlie\nGood\nMorning'
print(s)
s2 = '商品名\t\t单价\t数量\t总价'
s3 = '疯狂JAVA讲义\t108\t\t2\t\t216'
print(s2)
print(s3)
price = 108
print("the book's price is %s" % price)
user = "Charlie"
age = 8
# 格式话字符串中有两个占位符，第三部分也应该提供两个变量
print("%s is a %s years old boy" % (user, age))
num = -28
print('num is: %6i' % num)  # num is:    -28
print('num is: %6d' % num)  # num is:    -28
print('num is: %6o' % num)  # num is:    -34
print('num is: %6x' % num)  # num is:    -1c
print('num is: %6X' % num)  # num is:    -1C
print('num is: %6s' % num)  # num is:    -28
num2 = 30
# 最小宽度为6，左边补0
print('num2 is: %06d' % num2)  # num2 is: 000030
# 最小宽度为6，左边补0，带上符号
print('num2 is: %+06d' % num2)  # num2 is: +00030
# 最小宽度为6，右对齐
print('num2 is: %-6d' % num2)  # num2 is: 30____
print('num2 is: %-+06d' % num2)  # num2 is: +30___
my_value = 3.1415926535
# 最小宽度为8，小数点后保留3位，会进行四舍五入
print('my_value is: %8.3f' % my_value)  # my_value is:    3.142
# 最小宽度为8，小数点后保留3位，左边补0
print('my_value is: %08.3f' % my_value)  # my_value is: 0003.142
# 最小宽度为8，小数点后保留3位，左边补0，带符号
print('my_value is: %+08.3f' % my_value)  # my_value is: +003.142
print('my_value is: %-+08.3f' % my_value)  # my_value is: +3.142__
print('my_value is: %-+8f' % my_value)  # my_value is: 3.141593
print('my_value is: %+8f' % my_value)  # my_value is: +3.141593

the_name = 'Charlie'
# 只保留3个字符
print('the name is : %.3s' % the_name)  # the name is : Cha
# 只保留2个字符，最小宽度为10
print('the name is %10.3s' % the_name)  # the name is        Cha
print('the name is %-10.3s' % the_name)  # the name is Cha_______
