scores = {'语文': 89,
          '数学': 92,
          '英语': 93}
print(scores)  # {'语文': 89, '数学': 92, '英语': 93}  {key1:value1,key2:value2……}
print(type(scores))  # <class 'dict'>
empty_dict = {}
print(empty_dict)  # {}
dict2 = {(20, 30): 'good', 30: 'bad'}  # 使用元组作为key
print(dict2)  # {(20, 30): 'good', 30: 'bad'}
# dict2 = {[20, 30]: 'good', 30: 'bad'}  # 列表不能作为key

vegetables = [('celery', 1.58), ('brocoli', 1.29), ('lettuce', 2.19)]
dict3 = dict(vegetables)  # 建议使用(Mapping) (Iterable[Tuple[Any, Any]])
print(dict3)  # {'celery': 1.58, 'brocoli': 1.29, 'lettuce': 2.19}
dict3.clear()
vegetables = (['celery', 1.58], ['brocoli', 1.29], ['lettuce', 2.19])
dict3 = dict(vegetables)  # 不建议将嵌套列表转化为字典
print(dict3)  # {'celery': 1.58, 'brocoli': 1.29, 'lettuce': 2.19}
dict3.clear()
vegetables = (('celery', 1.58), ('brocoli', 1.29), ('lettuce', 2.19))
dict3 = dict(vegetables)
print(dict3)  # {'celery': 1.58, 'brocoli': 1.29, 'lettuce': 2.19}
cars = [['BWM', 8.5], ['BENS', 8.3], ['AUDI', 7.9]]
dict4 = dict(cars)  # 不建议将嵌套序列转化为字典
print(dict4)  # {'BWM': 8.5, 'BENS': 8.3, 'AUDI': 7.9}

dict5 = dict()  # 不增加()将会变成一种type
print(dict5)

dict6 = dict(spinach=1.39, cabbage=2.59)  # 关键字不需要加引号
print(dict6)  # {'spinach': 1.39, 'cabbage': 2.59}

scores = {'语文': 89}
print(scores['语文'])
scores['数学'] = 93
scores[93] = 5.7
print(scores)  # {'语文': 89, '数学': 93, 93: 5.7} 可通过对不存在的key赋值来增加字典key-value对
del scores[93]
print(scores)  # {'语文': 89, '数学': 93} 通过del删除key-value对

cars = {'BWM': 8.5,
        'BENS': 8.3,
        'AUDI': 7.9}
print(cars)  # {'BWM': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
cars['BENS'] = 4.3
cars['AUDI'] = 3.8
print(cars)  # {'BWM': 8.5, 'BENS': 4.3, 'AUDI': 3.8}
print('AUDI' in cars)  # True
print('PORSCHE' in cars)  # False
print('LAMBORGHINI' not in cars)  # True

print(cars.get('BWM'))  # 8.5 等效于car['BWM']
print(cars.get('PORSCHE'))  # None key不存在于字典时，返回None。car['PORSCHE']会导致KeyError错误

cars.update({'BWM': 4.5, 'PORSCHE': 9.3})
print(cars)  # {'BWM': 4.5, 'BENS': 4.3, 'AUDI': 3.8, 'PORSCHE': 9.3} 已存在的key会对value更新，不存在的key会增加key-value对
cars.update([('BWM', 8.5), ('BENS', 5.3)])
print(cars)  # {'BWM': 8.5, 'BENS': 5.3, 'AUDI': 3.8, 'PORSCHE': 9.3} 可以使用迭代元组进行更新
cars.update(BWM=4.3, BENS=8.5)
print(cars)  # {'BWM': 4.3, 'BENS': 8.5, 'AUDI': 3.8, 'PORSCHE': 9.3} 可以使用关键字参数进行更新

cars.clear()
print(cars)  # {}

cars = {'BWM': 8.5,
        'BENS': 8.3,
        'AUDI': 7.9}
ims = cars.items()
print(ims)  # dict_items([('BWM', 8.5), ('BENS', 8.3), ('AUDI', 7.9)])
print(type(ims))  # <class 'dict_items'>  针对dict_items,Python不希望进行直接操作，建议通过list转化为列表进行操作
print(list(ims))  # [('BWM', 8.5), ('BENS', 8.3), ('AUDI', 7.9)]
print(list(ims)[1])  # ('BENS', 8.3) 访问索引1的key-value
kys = cars.keys()
print(kys)  # dict_keys(['BWM', 'BENS', 'AUDI'])
print(type(kys))  # dict_keys
print(list(kys))  # ['BWM', 'BENS', 'AUDI']
print(list(kys)[1])  # BENS 访问索引1的key
vals = cars.values()
print(vals)  # dict_values([8.5, 8.3, 7.9])
print(type(vals))  # dict_values
print(list(vals))  # [8.5, 8.3, 7.9]
print(list(vals)[1])  # 8.3

print(cars.pop('AUDI'))  # 7.9 返回了'AUDI'对应的值
print(cars)  # {'BWM': 8.5, 'BENS': 8.3} 删除了相应的key-value

k, v = cars.popitem()  # 根据FILO原则出栈最后一个item，并返回(key,value)的元组，可通过解包赋值
print(k, v)  # BENS 8.3
print(cars)  # {'BWM': 8.5}

cars = {'BMW': 8.5,
        'BENS': 8.3,
        'AUDI': 7.9}
print(cars.setdefault('PORSCHE', 9.2))  # 9.2 字典中不存在，返回默认值，并添加进字典中
print(cars)  # {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9, 'PORSCHE': 9.2}
print(cars.setdefault('BMW', 2))  # 8.5 在字典中存在的话，不会更改value值

a_dict = dict.fromkeys(['a', 'b'])
print(a_dict)  # {'a': None, 'b': None}
b_dict = dict.fromkeys((13, 17))
print(b_dict)  # {13: None, 17: None}
c_dict = dict.fromkeys([12, 14], 'good')
print(c_dict)  # {12: 'good', 14: 'good'} 可设定默认value，赋予所有的keys
d_dict = dict.fromkeys([123, 123, 234, 234])
print(d_dict)  # {123: None, 234: None} 如输入的列表有重复值，会自动删除重复值

temp = '书名是：%(name)s，价格是：%(price)010.2f，出版社是：%(publish)s'
book = {'name': '疯狂Python讲义', 'price': 88.9, 'publish': '电子工业出版社'}
print(temp % book)  # 书名是：疯狂Python讲义，价格是：0000088.90，出版社是：电子工业出版社
print('书名是%(name)s,价格是%(price).2f，出版社是%(publish)s' % book)
