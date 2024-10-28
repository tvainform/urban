my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

key = 0
while key < len(my_list):
    if my_list[key] >= 0:
        if my_list[key] != 0:
            print(my_list[key])
        key += 1
        continue
    else:
        break