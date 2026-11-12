# Рекурсия
# Факториал числа

#
# n = 1 -> 1
# n = 2 -> 1 * 2 = 2
# n = 3 -> 1 * 2 * 3 = 6
# otvet = 1
# for i in range(1,5):
#     otvet = otvet * i
# print(otvet)

# def factorial(n):
#     # Базовый случай
#     if n == 1:
#         return 1
#     # Рекурсивный шаг
#     return n * factorial(n-1)
# print(factorial(5))

# factorial(5) = 5 * factorial(4) = 5 * 24 = 120

# factorial(4) = 4 * factorial(3) = 4 * 6 = 24

# factorial(3) = 3 * factorial(2) = 3 * 2 = 6

# factorial(2) = 2 * factorial(1)  = 2

# factorial(1) = 1
# 0,1,1,2,3,5,8
# 0,1,2,3,4,5

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1
#     # Рекурсивный
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(6))

# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     # Базовый случай
#     if n <= 1:
#         return 1
#     if n == 2:
#         return 2
#     # Рекурсивный шаг
#     return 5 * f(n-1) - f(n-2)
# for n in range(5622):
#     f(n)
# print(f(5621))

from functools import lru_cache
@lru_cache(100)
def f(n):
    if n < 10:
        return 1
    if n >= 10:
        return (n+3) * f(n-3)

for n in range(10,247564):
    if n == 247563:
        x1 = f(n)
    elif n == 247560:
        x2 = f(n)
    elif n == 247557:
        x3 = f(n)
    else:
        f(n)
print((x1 // 519 - 477 * x2) // x3)

