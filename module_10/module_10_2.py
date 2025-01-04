# Задача "За честь и отвагу!":
import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.counter = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        day = 0
        while self.counter:
            self.counter -= self.power
            day += 1
            print(f'{self.name} сражается {day} день(дня)..., осталось {self.counter} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')