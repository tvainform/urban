immutable_var = ('string', True, 10, 5.2, ['one','two', 'three'])
print(immutable_var)

# при попытке изменить элемент кортежа типа <class 'str'> возникает ошибка, т.к. кортеж - это неизменяемый объект
# immutable_var[0] = 'new_string'
# Traceback (most recent call last):
#   File "D:\Projects\urban\module_1_5.py", line 4, in <module>
#     immutable_var[0] = 'new_string'
#     ~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

# при попытке изменить элемент кортежа типа <class 'list'> ошибка не возникает
immutable_var[4][0] = 'zero'
print(immutable_var) # ('string', True, 10, 5.2, ['zero', 'two', 'three'])

mutable_list = ['111', '222', '333', 444]
mutable_list[0] = '000'
print(mutable_list) # ['000', '222', '333', '444']