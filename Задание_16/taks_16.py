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

# from functools import lru_cache
# @lru_cache(100)
# def f(n):
#     if n < 10:
#         return 1
#     if n >= 10:
#         return (n+3) * f(n-3)
# for n in range(10,247564):
#     if n == 247563:
#         x1 = f(n)
#     elif n == 247560:
#         x2 = f(n)
#     elif n == 247557:
#         x3 = f(n)
#     else:
#         f(n)
# print((x1 // 519 - 477 * x2) // x3)

# from functools import lru_cache
# @lru_cache(100)
# def f(n):
#     return 3 * g(n-3)+7
# @lru_cache(100)
# def g(n):
#     if n <= 20:
#         return n + 2
#     if n > 20:
#         return g(n-3) + 1
# for n in range(1,37812):
#     f(n)
# for n in range(21, 37809): # f(37811) = 3 * g(37808) + 7, g(37809) - максимальный вызов функции g(n)
#     g(n)
# print(f(37811))


# from functools import lru_cache
# @lru_cache(100)
# def f(n):
#     if n >= 21:
#         return f(n-8) + 1095 # Рекурсивный случай
#     if n < 21:
#         return 10 * (g(n-7) - 36) # Базовый случай
# @lru_cache(100)
# def g(n):
#     if n >= 22560:
#         return n // 23 + 33 # Базовый случай
#     if n < 22560:
#         return g(n+11) - 4 # Рекурсивный случай
# for n in range(22560,1,-1): g(n)
# for n in range(21, 550):  f(n)
# print(f(548))
# f(550) = f(n-8) + 1095
# f(542) = f(542-8) + 1095
# ...
# ...
# ...
# f(20) = 10 * (g(13) - 36))


