import requests
from json import JSONDecoder
import numpy as np
from PIL import Image, ImageOps, ImageEnhance


# библиотека requests
# данный код парсит страницу товара на сайте poizon.com
# ищет в коде страницы все строки в формате json
# выводит в консоль найденный json с ключом props
# использованы методы класса requests: get, text, status_code
req = requests.get('https://www.poizon.com/product/nike-blazer-mid-77-jumbo-white-black-52430952')
def extract_json_objects(text, decoder=JSONDecoder()):
    pos = 0
    while True:
        match = text.find('{', pos)
        if match == -1:
            break
        try:
            result, index = decoder.raw_decode(text[match:])
            yield result
            pos = match + index
        except ValueError:
            pos = match + 1

if req.status_code == 200:
    for line in extract_json_objects(req.text):
        try:
            print(line['props'])
            break
        except:
            pass

# библиотека numpy
# данный код создает 2 структуры данных с помощью класса numpy
# выполняет слияние этих структур
# выводит в консоль размер получившейся структуры
# выводит в консоль размерность получившейся структуры
a = np.arange(10)
b = np.arange(10, 20)
c = np.concatenate((a, b))
print(c.size)
print(c.ndim)

# библиотека pillow (PIL)
# данный код открывает подготовленную картинку
# выводит в консоль его размеры
# уменьшает его размеры и сохраняет уменьшенную копию рядом с оригиналом
# затем открывает уменьшенную копию, увеличивает ее контраст на 30% и открывает во внешнем просмотрщике
with Image.open('topwens.png') as im:
    print('topwens.png', im.format, f"{im.size}x{im.mode}")
    size = (150, 150)
    ImageOps.contain(im, size).save("topwens-150-150.png")

with Image.open('topwens-150-150.png') as im:
    enh = ImageEnhance.Contrast(im)
    enh.enhance(1.3).show("на 30% больше контрастности")