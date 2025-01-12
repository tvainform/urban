# Задача "Многопроцессное считывание":
from multiprocessing import Pool
import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while line := f.readline():
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    # Линейный вызов
    start_1 = datetime.datetime.now()
    for file in filenames:
        read_info(file)
    end_1 = datetime.datetime.now()
    print(f'{end_1 - start_1} (линейный)')

    # Многопроцессный
    start_2 = datetime.datetime.now()
    with Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)

    end_2 = datetime.datetime.now()
    print(f'{end_2 - start_2} (многопроцессорный)')