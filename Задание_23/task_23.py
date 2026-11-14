def f13(start, end):
    if start == end:
        return 1
    if start > end: # из 2 в 7
        return 0
    return f13(start + 4,end) + f13(start * 2,end)
print(f13(13,42))

def f13(start, end):
    if start == end:
        return 1
    if start > end: # из 2 в 7
        return 0
    return f13(start + 1,end) + f13(start + 3,end) + f13(start * 3,end)
print(f13(3,9) * f13(9,27) *f13(27,31))

# Грозный -> Аргун, Аргун -> Гудермес -> Куда-нибудь

def f13(start, end):
    if start == end:
        return 1
    if start < end or start == 32: # Не содержит
        return 0
    return f13(start - 2, end) + f13(start - 5,end) + f13(start // 3, end)
print(f13(46, 19) * f13(19,7))
