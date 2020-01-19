repository = {}  # 定义仓库 {id:(id,name,price)……}
shop_list = []  # 定义购物清单 [[id,number]……]


# 函数：初始化商品
def init_repository():
    goods1 = ('10000001', '疯狂Ruby讲义', 88.0)
    goods2 = ('10000002', '疯狂Swift讲义', 69.0)
    goods3 = ('10000003', '疯狂Kotlin讲义', 59.0)
    goods4 = ('10000004', '疯狂Java讲义', 109.0)
    goods5 = ('10000005', '疯狂Android讲义', 108.0)
    goods6 = ('10000006', '疯狂iOS讲义', 77.0)
    repository[goods1[0]] = goods1
    repository[goods2[0]] = goods2
    repository[goods3[0]] = goods3
    repository[goods4[0]] = goods4
    repository[goods5[0]] = goods5
    repository[goods6[0]] = goods6


# 函数：显示尝试的商品清单，遍历仓库dict字典
def show_goods():
    print('欢迎光临 小小超市')
    print('我们的商品清单：')
    print('%13s%40s%10s' % ('条码', '商品名称', '价格'))  # %13s中13个字符，中文占2个字符，所以比下面少2
    # <editor-fold desc="遍历代表所有values来显示商品">
    for goods in repository.values():
        print('%15s%40s%12s' % goods)
    # </editor-fold>


# 函数：显示购物清单，遍历shop_list中的元素
def show_list():
    print('=' * 100)
    # 当list为空时，不输出清单
    if not shop_list:
        print('还未购买商品')
    else:
        title = '%-5s|%15s|%40s|%10s|%4s|%10s' % \
                ('ID', '条码', '商品名称', '单价', '数量', '小计')
        print(title)
        print('-' * 100)
        sum_price = 0
        # enumerate枚举列表，生成一个[(0,seq[0]),(1,seq[1]……]的列表
        for i, item in enumerate(shop_list):
            list_id = i + 1  # 索引
            code = item[0]  # 条码
            name = repository[code][1]  # 书名
            price = repository[code][2]  # 单价
            number = item[1]  # 数量
            amount = price * number  # 小计
            sum_price += amount  # 总价
            line = '%-5s|%17s|%40s|%12s|%6s|%12s' % \
                   (list_id, code, name, price, number, amount)
            print(line)
        print('-' * 100)
        print(' ' * 10, '总计：', sum_price)


# 添加购买的商品
def add():
    # 输入条码
    code = input('请输入商品的条码：\n')
    # 没找到对应的商品，报错
    if code not in repository.keys():
        print('条码错误，请重新输入')
        return
    # 根据条码找商品
    goods = repository[code]
    number = input('请输入购买的数量：\n')
    shop_list.append([code, int(number)])


# 修改购物清单
def edit():
    edit_id = input('请输入需要修改的购物明细项ID：\n')
    index = int(edit_id) - 1
    item = shop_list[index]
    number = input('请输入新的购买数量：\n')
    item[1] = int(number)


# 删除购物清单项
def delete():
    delete_id = input('请输入需要修改的购物明细项ID：\n')
    index = int(delete_id) - 1
    del shop_list[index]


# 结账并退出程序
def payment():
    # 先打印清单
    show_list()
    print('\n' * 3)
    print('欢迎光临')
    # 退出程序
    import os
    os._exit(0)


# 定义命令清单
cmd_dict = {'a': add, 'e': edit, 'd': delete, 'p': payment, 's': show_goods}


# 输出命令
def show_command():
    cmd = input('请输入操作指令：\n' + '  添加(a)  修改(e)  删除(d)  结算(p)  超市商品(s)\n')
    if cmd not in cmd_dict:
        print('未找到可执行的命令，请重新输入')
    else:
        cmd_dict[cmd]()


init_repository()
show_goods()
# 重复输出商品列表和命令列表
while True:
    show_list()
    show_command()
