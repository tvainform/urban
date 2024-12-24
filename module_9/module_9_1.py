# Задача "Вызов разом":

def apply_all_func(int_list, *functions):
    results = {}
    for f in functions:
        results[f.__name__ ] = f(list(map(int, int_list)))
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))