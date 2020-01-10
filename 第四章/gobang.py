import random

board_size = 8
board = []


def init_board():
    # 定义一个二维列表充当棋盘
    # 为实现X*Y的二位列表，需要使用for来实现
    for i in range(board_size):
        row = ['＋'] * board_size
        board.append(row)


def board_print():
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j], end='  ')
        print()


def get_value():
    if input_str.count(',') == 1:
        str1, str2 = input_str.split(sep=',')
        if int(str1) in range(1, board_size + 1) and int(str2) in range(1, board_size + 1):
            return int(str1), int(str2)
        else:
            return 1  # '超过范围'
    elif input_str.count('，') == 1:
        str1, str2 = input_str.split(sep='，')
        if int(str1) in range(1, board_size + 1) and int(str2) in range(1, board_size + 1):
            return int(str1), int(str2)
        else:
            return 1  # '超出范围'
    elif input_str == 'esc':
        return 'esc'
    else:
        return 0  # 输入错误


def computer():
    i = random.randint(0, board_size - 1)
    j = random.randint(0, board_size - 1)
    while board[i][j] != '＋':
        i = random.randint(0, board_size - 1)
        j = random.randint(0, board_size - 1)
    board[i][j] = '◍'


# 结果判断 0：平局 1:胜利 2:失败
def rule():
    # 平局确认
    count = 0
    for i in range(0, board_size):
        count += board[i].count('＋')
    if count == 0:
        # print('棋盘已满，平局')
        return 0  # 0：平局
    # 纵向判断
    for i in range(0, board_size - 5):
        for j in range(0, board_size):
            count_list = []
            for n in range(0, 5):
                count_list.append(board[i + n][j])
                if count_list.count('▤') == 5:
                    # print('恭喜你赢了')
                    return 1  # 1:胜利
                if count_list.count('◍') == 5:
                    # print('你输了')
                    return 2  # 2:失败
    # 横向判断
    for i in range(0, board_size):
        for j in range(0, board_size - 5):
            count_list = []
            for n in range(0, 5):
                count_list.append(board[i][j + n])
                if count_list.count('▤') == 5:
                    # print('恭喜你赢了')
                    return 1  # 1:胜利
                if count_list.count('◍') == 5:
                    # print('你输了')
                    return 2  # 2:失败
    # 右斜向判断
    for i in range(0, board_size - 5):
        for j in range(0, board_size - 5):
            count_list = []
            for n in range(0, 5):
                count_list.append(board[i + n][j + n])
                if count_list.count('▤') == 5:
                    # print('恭喜你赢了')
                    return 1  # 1:胜利
                if count_list.count('◍') == 5:
                    # print('你输了')
                    return 2  # 2:失败
    # 左斜向判断
    for i in range(0, board_size - 5):
        for j in range(0, board_size - 5):
            count_list = []
            for n in range(0, 5):
                count_list.append(board[-1 - i - n][-1 - j - n])
                if count_list.count('▤') == 5:
                    # print('恭喜你赢了')
                    return 1  # 1:胜利
                if count_list.count('◍') == 5:
                    # print('你输了')
                    return 2  # 2:失败


init_board()
board_print()
input_str = input('请输入您下棋的坐标（1~%d），应以x,y的格式，输入"esc"退出：\n' % board_size)
value = get_value()
while value != 'esc':
    if value == 0:
        input_str = input('输入错误，应以x,y的格式，输入"esc"退出：\n')
        value = get_value()
    elif value == 1:
        input_str = input('数值超出范围（1~%d），输入"esc"退出：\n' % board_size)
        value = get_value()
    else:
        x_int, y_int = value
        if board[x_int - 1][y_int - 1] != '＋':
            input_str = input('该坐标已存在，请重新输入：\n')
            value = get_value()
            continue
        board[x_int - 1][y_int - 1] = '▤'
        computer()
        board_print()
        value = rule()
        if value == 0:
            print('棋盘已满，平局')
            break
        elif value == 1:
            print('恭喜你，你赢了')
            break
        elif value == 2:
            print('真遗憾，你输了')
            break
        else:
            input_str = input('请输入您下棋的坐标（1~%d），应以x,y的格式，输入"esc"退出：\n' % board_size)
            value = get_value()
print('退出')
