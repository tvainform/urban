# Задача "Записать и запомнить":

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    result = {}
    for k,i in enumerate(strings):
        result[(k+1,file.tell())] = i
        file.write(f'{i}\n')

    file.close()
    return result


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)