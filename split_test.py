s = 'crazyit.org is a good site'
# 使用空白对字符串进行分割
print(s.split())
# 使用空白对字符串进行分割，最多只分割前两个单词，其余合并为一个字符串
print(s.split(None, 2))
# 使用点进行分割
print(s.split('.'))
my_list = s.split()
print(my_list)
print('/'.join(my_list))
print(','.join(my_list))
print('\t'.join(my_list))
