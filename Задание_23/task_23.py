# def f13(start, end):
#     if start == end:
#         return 1
#     if start > end: # из 2 в 7
#         return 0
#     return f13(start + 4,end) + f13(start * 2,end)
# print(f13(13,42))

# def f13(start, end):
#     if start == end:
#         return 1
#     if start > end: # из 2 в 7
#         return 0
#     return f13(start + 1,end) + f13(start + 3,end) + f13(start * 3,end)
# print(f13(3,9) * f13(9,27) * f13(27,31))

# Грозный -> Аргун, Аргун -> Гудермес -> Куда-нибудь

# def f13(start, end):
#     if start == end:
#         return 1
#     if start < end or start == 32: # Не содержит
#         return 0
#     return f13(start - 2, end) + f13(start - 5,end) + f13(start // 3, end)
# print(f13(46, 19) * f13(19,7))



# №31510
# def f23(start,end):
#     if start == end: return 1
#     if start > end: return 0
#     s = str(start)
#     if s[1] < s[2]: # Десятков меньше чем единиц
#         return f23(start + 1,end) + f23(int(s[0] + s[2] + s[1]),end)
#     else:
#         return f23(start + 1,end)
#
# print(f23(100,141))


# №31367
# def f23(start,end):
#     if start == end: return 1
#     if start > end: return 0
#     s = str(start)
#     if '1' in s:
#     #if s.count('1') > 0:
#         return f23(start+1, end) + f23(int(s.replace('1','3')),end)
#     else:
#         return f23(start + 1,end)
# print(f23(11,94))
#if '1' in s:

#print('11'.replace('1','3',1)) - замена одной единицы на тройку.

# def f23(start,end):
#     if start == end: return 1
#     if start > end: return 0
#     return f23(start + 1, end) + f23(bin(start)[2:].count('1') + start,end)
# print(f23(5,40))


# №31417
# def f23(start,end):
#     if start == end: return 1
#     if start > end: return 0
#     s = str(start)
#     if sum(map(int,s)) < 10:
#         return f23(start + 1,end) + f23(int(s + str(sum(map(int,s)))),end)
#     else:
#         return f23(start + 1,end)
# print(f23(3,200))