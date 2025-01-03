def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i

for number in even_numbers_generator(10):
    print(number)

def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

for number in fibonacci_generator(20):
    print(number)
