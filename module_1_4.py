my_string = input('Введите произвольный текст: ')
print(len(my_string)) #Вывести количество символов введённого текста
print(my_string.upper()) #Вывести строку my_string в верхнем регистре
print(my_string.lower()) #Вывести строку my_string в нижнем регистре
my_string = my_string.replace(' ', '') #Измените строку my_string, удалив все пробелы
print(my_string[0]) #Выведите первый символ строки my_string
print(my_string[-1]) #Выведите последний символ строки my_string