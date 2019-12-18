a = 'abcdefghijklmnopqrstuvwxyz'
print(a[2:8:3])  # cf 获取索引2到索引8的子串，步长为3
print(a[2:8:2])  # ceg 不包含索引8
print(a[2:8:1])  # cdefgh 默认步长1
print(a[2:8])  # cdefgh
