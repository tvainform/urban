# Задание: Декораторы в Python

def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        prime = 'Простое'
        if n <= 1:
            prime = 'Составное'
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    prime = 'Составное'
                    break
        print(prime)
        return n
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)