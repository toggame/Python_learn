size = int(input('请输入一个整数：'))
# size = 5  # 测试
array = [[0] * size]
for i in range(size - 1):
    array += [[0] * size]
rotate = 0  # 旋转方向
row, column = 0, 0  # 行号和列号
n = size  # 控制循环
for i in range(1, size ** 2 + 1):
    array[row][column] = i
    # 当向下循环时
    if rotate == 0:
        row += 1
        # 当到达左下角时，更改旋转方向
        if row == n - 1:
            rotate = 1
    # 当向右循环时
    elif rotate == 1:
        column += 1
        # 当到达右下角时，更改旋转方向
        if column == n - 1:
            rotate = 2
    # 当向上循环时
    elif rotate == 2:
        row -= 1
        # 当到达右上角时，更改旋转方向，且控制循环数-1
        if row == size - n:
            rotate = 3
            n -= 1
    # 当向左循环时
    elif rotate == 3:
        column -= 1
        # 当到达左上角时，更改旋转方向
        if column == size - n:
            rotate = 0
# 遍历输出二维列表
for i in range(size):
    for j in range(size):
        print('%02d' % array[i][j], end=' ')  # 按空格分割
    print('')  # 补充换行符
