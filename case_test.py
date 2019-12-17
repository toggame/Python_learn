a = 'our domain is crazyit.org'
# 每个单词的首字母大写
print(a.title())
# 每个字母小写
print(a.lower())
# 每个字母大写
print(a.upper())

s = '  this is a puppy   '
# 删除左边的空白
print(s.lstrip())
# 删除右边的空白
print(s.rstrip())
# 删除两边的空白
print(s.strip())

s2 = 'i think it is a scarecrow'
# 删除左边的i t o w字符
print(s2.lstrip('itow'))  # 输出 think it is a scarecrow，包含关系
print(s2.lstrip('tow'))  # 输出i think it is a scarecrow
print(s2.rstrip('itow'))  # 输出i think it is a scarecr
print(s2.strip('itow'))  # 输出 think it is a scarecr
