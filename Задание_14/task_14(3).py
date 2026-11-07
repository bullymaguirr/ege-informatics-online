#x = число от 0 до 2999

#


# №23754
# for x in range(1,3000):
#     number = 9 * 11**210 + 8 * 11**150 - x
#     count = 0
#     while number > 0:
#         if (number % 11) == 0: # Нужно искать нули
#             count = count + 1 # Увеличиваем на 1
#         number = number // 11 # Теперь делим это число
#     if count == 60:
#         print(count,x)


# def f11(N):
#     count = 0
#     while N > 0:
#         if (N % 11) == 0:  # Нужно искать нули
#             count = count + 1  # Увеличиваем на 1
#         N = N // 11  # Теперь делим это число
#     return count # Сколько НУЛЕЙ В 11-ой записи
#
# for x in range(1,3000):
#     number = 9 * 11 ** 210 + 8 * 11 ** 150 - x
#     if f11(number) == 60:
#         print(x)

# № 24534
a = []
# Максимальное количество нулей
for x in range(1,11500):
    number = 7**270 + 7**170 + 7**70 - x
    chetchik = 0 # Количество нулей.
    while number > 0:
        if number % 7 == 0:
            chetchik = chetchik + 1
        number = number // 7
    if chetchik == 203:
        print(chetchik,x)
    #a.append(chetchik)
#print(max(a))
# 1) Подзадача 1: найти максимальное количество нулей
# 2) Подзадача 2: При каком x, количество нулей максимальное

