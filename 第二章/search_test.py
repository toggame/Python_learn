s = 'crazyit.org is a good site'
# 判断s是否以crazyit开头
print(s.startswith('crazyit'))
# 判断s是否以site结尾
print(s.endswith('site'))
# 查找s中的'org'出现的位置
print(s.find('org'))  # 8，以0为起始位
print(s.find('tgtg'))  # 输出-1
# 查找s中的'org'出现的位置
print(s.index('org'))  # 8，未找到会引发ValueError错误，不建议
#  从索引9处开始查找'org'出现的位置
print(s.find('or', 9))
print(s.find('org', 3, 11))  # 不包含end索引，返回结果和开始索引无关
# 将字符串中的所有it替换成xxxx
print(s.replace('it', 'xxxx'))  # 输出crazyxxxx.org is a good sxxxxe
print(s.replace('it', 'xxxx', 1))  # 输出crazyxxxx.org is a good site
# 定义翻译映射表
table = {97: 945, 98: 946, 116: 964}
print(s.translate(table))
table = str.maketrans('abt', 'αβτ')
print(s.translate(table))
