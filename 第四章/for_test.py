s_max = int(input('请输入您想计算的阶乘：'))
result = 1
for num in range(1, s_max + 1):
    result *= num
print(result)

for i in range(1, 5):
    print(i)
    i = 20  # 不建议在循环体中对循环计数器赋值
    print('i:', i)

a_tuple = ('crazyit', 'fkit', 'Charlie')
for ele in a_tuple:  # 可以以元组或列表进行遍历，循环计数器会依次赋值为元素的值，循环次数等于元素数量
    print('当前元素是：', ele)

src_list = [12, 45, 3.4, 13, 'a', 4, 56, 'crazyit', 109.5]
my_sum = 0
my_count = 0
for ele in src_list:
    if isinstance(ele, int) or isinstance(ele, float):
        print(ele)
        my_sum += ele
        my_count += 1
print('数值总和：', my_sum)
print('平均数：', my_sum / my_count)

a_list = [330, 1.4, 50, 'fkit', -3.5]
for i in range(0, len(a_list)):
    print('第%d个元素是%s' % (i, a_list[i]))

my_dict = {'语文': 89, '数学': 92, '英语': 80}
for key, value in my_dict.items():  # 注意一定要返回items，不然结果会变成key语value文
    print('key:', key)
    print('value:', value)
print('————————')
for key in my_dict.keys():
    print('key:', key)
    print('value:', my_dict[key])
print('————————')
for value in my_dict.values():
    print('value:', value)

src_list.clear()
n = int(input('请输入元素个数：'))
for i in range(0, n):
    src_list.append(input('请输入元素%d：' % i))
print(src_list)
statistics = {}
for ele in src_list:
    if ele in statistics:
        statistics[ele] += 1
    else:
        statistics[ele] = 1
for key, value in statistics.items():
    print('%s出现的次数为%d' % (key, value))

a_list = [330, 1.4, 50, 'fkit', -3.5]
for ele in a_list:
    print('元素：', ele)
else:
    print('else块：', ele)  # ele等于最后一次遍历的结果
print('循环体外：', ele)
