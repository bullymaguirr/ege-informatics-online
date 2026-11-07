
# for x in '0123456789ABCDEFGHIJKL':
#     num1 = int('27'+ x + '98876', 22)
#     num2 = int('26' + x + '51',22)
#     num3 = int('711' + x + '5',22)
#     main_num = num1 + num2 + num3
#     if main_num % 21 == 0: # Кратно 21
#         print(main_num // 21, x)

# № 27297
# from string import printable
# for x in printable[:19]:
#     num1 = int('2E'+x+'G8',19)
#     num2 = int('6F'+x+'BG',19)
#     main_num = num1 + num2
#     if main_num % 18 == 0:
#         print(main_num // 9, x)
from string import printable
for x in range(42):
    # J569x   1xIA
    # 43210   3210
    num1 = x * 42**0 + 9 * 42**1 + 6 * 42**2 + 5 * 42**3 + 19 * 42**4
    num2 = 10 * 42**0 + 18 * 42**1 + x * 42**2 + 1 * 42**3
    main_num = num1 + num2
    if main_num % 155 == 0:
        print(main_num // 155, x)

        #27298