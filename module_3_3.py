
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()                                # Вызов функции без аргументов
print_params(5, 'function', False)   # Вызов функции с тремя аргументами
print_params(466, 'urban')              # Вызов функции с двумя аргументами + 1 по умолчанию
print_params(a = 1985)                        # Вызов функции с одним аргументом + 2 по умолчанию

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [0, 'string', False]
values_dict = {'a': 2, 'b': 'dict', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)