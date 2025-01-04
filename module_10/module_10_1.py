# Задача "Потоковая запись в файлы":

from datetime import datetime
import time
from threading import Thread

start = datetime.now()

def wite_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')



wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

end = datetime.now()
print(f'Работа потоков %s' % (end - start))

start = datetime.now()

tread1 = Thread(target=wite_words, args=(10, 'example5.txt'))
tread2 = Thread(target=wite_words, args=(30, 'example6.txt'))
tread3 = Thread(target=wite_words, args=(200, 'example7.txt'))
tread4 = Thread(target=wite_words, args=(100, 'example8.txt'))

tread1.start()
tread2.start()
tread3.start()
tread4.start()

tread1.join()
tread2.join()
tread3.join()
tread4.join()

end = datetime.now()
print(f'Работа потоков %s' % (end - start))