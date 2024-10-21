# 2. Работа со словарями:
my_dict = {'name': 'Vadim', 'age': 39}
print(my_dict)
print(my_dict['name']) # Выведите на экран одно значение по существующему ключу
print(my_dict.get('weight', 'Такого ключа нет')) # Выведите на экран одно значение по отсутствующему из словаря my_dict без ошибки
my_dict['eye_color'] = 'brown' # Добавьте ещё две произвольные пары того же формата в словарь my_dict
my_dict['weight'] = 80 # Добавьте ещё две произвольные пары того же формата в словарь my_dict
del_item = my_dict.pop('age') # Удалите одну из пар в словаре по существующему ключу из словаря my_dict
print(del_item) # и выведите значение из этой пары на экран
print(my_dict)

# 3. Работа с множествами:
my_set = {'zero', 1.5, 2, 3, 4, 3, 1, 4, 1.5}
print(my_set)
my_set.add('string')
my_set.add(('a','b','c'))
print(my_set)
print(my_set.discard(1.5))
print(my_set)