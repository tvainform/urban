first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x) - len(y)) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[k]) == len(second[k]) for k in range(0, len(first)))

print(list(first_result))
print(list(second_result))