# Задача "Ошибка эволюции
from random import randint

class Animal:
    live = True
    sound = None #звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0 #степень опасности существа
    def __init__(self, speed):
        self._cords = [0,0,0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
            return
        else:
            self._cords = [i * self.speed for i in [dx, dy, dz]]

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0" )

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True #наличие клюва
    def lay_eggs(self):
        print(f"Here are(is) {randint(1,4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        while self._cords[2] > 0:
            self._cords[2] -= abs(dz)
            self.speed /= 2

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()