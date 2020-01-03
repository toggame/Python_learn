han_list = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']  # 数值转换文本列表
unit_list = ['拾', '佰', '仟']  # 数值单位列表


# 把一个浮点数分解成整数部分和小数部分字符串
# num是需要被分解的浮点数(float)
# 返回分解出来的整数部分和小数部分(str)
# 第一数组元素是整数部分，第二个数组元素是小数部分
def divide(num):
    # 将一个浮点数强制类型转换为int类型，即可得到它的整数部分
    integer_num = int(num)
    # 浮点减去整数部分，得到小数部分，小数部分乘以100后再取整，得到2位小数，因num参与了计算，num必须为int或float
    # fraction = int(round(num - integer, 2) * 100)
    fraction_num = round((num - integer_num) * 100)  # round默认返回int，如给了小数位数，则返回值与原数据格式一致
    return str(integer_num), str(fraction_num)


# 把1个4位的数字字符串变成汉字字符串
# num_str是需要被转换的4位数字字符串(str)
# 返回4位数字字符串被转换成汉字字符串(str)
def four_to_han_str(num_str):
    result = ''
    num_len = len(num_str)
    # 依次遍历数字字符串的每一位数字
    for i in range(num_len):
        num = int(num_str[i])
        # 最后一位为0时，不输出
        if i == num_len - 1 and num == 0:
            continue
        # 当不是最后一位且不为0时，带单位输出
        elif i != num_len - 1 and num != 0:
            result += han_list[num] + unit_list[-(4 - num_len + i) - 1]
        # 当连续2个0时，推后输出
        elif i < num_len - 1 and num_str[i] == num_str[i + 1] == '0':
            continue
        # 最后一位或非最后一位0时，仅输出汉字，不添加单位
        else:
            result += han_list[num]
    return result


# 把整数部分数字字符串变成汉字字符串
# num_str是需要被转换的数字字符串(str)
# 返回数字字符串被转换成汉字字符串(str)
def integer_to_str(num_str):
    str_len = len(num_str)
    n8 = (str_len - 1) // 8 + 1
    result = ''
    for i in range(1, n8 + 1):
        # 5位数以下不添加'万'，直接输出后四位+'圆'
        if str_len < 5:
            result += four_to_han_str(num_str[-4:]) + '圆'
        # 如果是最后一次遍历，不需要添加'亿'
        elif i == n8:
            # 如果-8：-4不为空，添加'万'
            if four_to_han_str(num_str[-8:-4]) != '':
                # 当为4个0时，添加零
                if four_to_han_str(num_str[-8:-4]) == '0000':
                    result += '零' + four_to_han_str(num_str[-4:]) + '圆'
                # 当不为'0000'时，添加'万'
                else:
                    result += four_to_han_str(num_str[-8:-4]) + '万' + four_to_han_str(num_str[-4:]) + '圆'
            # 如果-8到-4位是空，不输出'万'
            else:
                result += four_to_han_str(num_str[-4:]) + '圆'
        # 其他时候遍历，当小于5位时直接添加'亿'
        elif str_len - 8 * (n8 - i) < 5:
            result += four_to_han_str(num_str[-8 * (n8 + 1 - i) + 4:-8 * (n8 + 1 - i) + 8]) + '亿'
        # 如果前4为不为空，输出'万'
        elif four_to_han_str(num_str[-8 * (n8 + 1 - i):-8 * (n8 + 1 - i) + 4]) != '':
            # 当为4个0时，添加'零'
            if four_to_han_str(num_str[-8 * (n8 + 1 - i):-8 * (n8 + 1 - i) + 4]) == '0000':
                result += '零' + four_to_han_str(num_str[-8 * (n8 + 1 - i) + 4:-8 * (n8 + 1 - i) + 8]) + '亿'
            # 当不为'0000'时，添加'万'
            else:
                result += four_to_han_str(num_str[-8 * (n8 + 1 - i):-8 * (n8 + 1 - i) + 4]) + '万' + \
                          four_to_han_str(num_str[-8 * (n8 + 1 - i) + 4:-8 * (n8 + 1 - i) + 8]) + '亿'
        # 如果前4位为空，不输出'万'
        else:
            result += four_to_han_str(num_str[-8 * (n8 + 1 - i) + 4:-8 * (n8 + 1 - i) + 8]) + '亿'
        # 其他遍历，位数小于5时直接添加'亿'
    # 当以壹拾开头时，删掉第一个'壹'
    if result[0:2] == '壹拾':
        result = result[1:]
    return result


# 把小数部分数字字符串变成汉字字符串
# num_str是需要被转换的数字字符串(str)
# 返回数字字符串被转换成汉字字符串(str)
def fraction_to_str(num_str):
    num_len = len(num_str)
    # 当长度为1时（对应0.00~0.09）
    if num_len == 1:
        # 为0时，不输出小数位
        if num_str == '0':
            return ''
        # 不为0时，输出零几分
        else:
            return '零' + han_list[int(num_str[0])] + '分'
    # 当对应0.10、0.20、0.30……
    elif num_str[1] == '0':
        return han_list[int(num_str[0])] + '角'
    else:
        return han_list[int(num_str[0])] + '角' + han_list[int(num_str[1])] + '分'


input_num = float(input('请输入一个浮点数：'))
# input_num = 10210201001.65  # 测试
integer, fraction = divide(input_num)
print('转换后的结果为：%s%s' % (integer_to_str(integer), fraction_to_str(fraction)))
# 当浮点数超过双浮点范围时，会自动采用科学计数，导致结果不准确
