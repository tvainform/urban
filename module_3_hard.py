summa = 0

def calculate_structure_sum(data):
    global summa
    if isinstance(data, int):
        summa += data
    elif isinstance(data, str):
        summa += len(data)
    elif isinstance(data, (tuple,set,dict,list)):
        for i in data:
            calculate_structure_sum(i)
            if isinstance(data, dict):
                calculate_structure_sum(data[i])
    return summa

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)

print(result)
