books = ['书名1', '书名2', '书名3']
prices = [79, 69, 89]
for book, price in zip(books, prices):
    print('%s的价格为:%3.2f' % (book, price))

my_list = ['fkit', 'crazyit', 'Charlie', 'fox', 'Emily']
for s in sorted(my_list, key=len):  # 按长度排序，不改变原列表
    print(s)
print(my_list)
for s in reversed(my_list):  # 反向列表，不改变原列表
    print(s)
print(my_list)
