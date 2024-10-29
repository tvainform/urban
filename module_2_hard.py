def get_pass(n):
    arr = []
    for j in range(1, n):
        for k in range(1, n):
            if k > j and n % (j + k) == 0:
                arr.append(f'{j}{k}')
    return arr

# функция выводит пароли для чисел от 3 до 20
def print_pass_all():
    for i in range(3, 21):
        arr = []
        for j in range(1, i):
            for k in range(1, i):
                if k > j and i % (j + k) == 0:
                    arr.append(f'{j}+{k}')
        print(i, arr)

while True:
    number = int(input('Введите первое число (3 - 20): '))
    if 3 <= number <= 20:
        print(number,'-',''.join(get_pass(number)))
        print('------------------------------------')
        print('Данные для проверки:')
        print_pass_all()
        break
    else:
        print(f'Введено некорректное число ({number})')