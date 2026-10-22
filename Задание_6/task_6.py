# № 31503
# from turtle import * ctrl + /
# tracer(0)
# screensize(5000,5000)
# m = 20 #Масштаб
# for i in range(6):
#     forward(24*m); right(90);forward(30*m); right(90)
# up()
# forward(2*m)
# right(90)
# forward(10*m)
# left(90)
# down()
# for i in range(6):
#     forward(75*m); right(90); forward(71*m); right(90)
# # Как нарисовать систему координат
# up()
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x*m,y*m)
#         dot(4, 'red')
# done()

# № 31214

# Объединение = Суммированная площадь всех фигур минус пересечение.
# from turtle import *
# screensize(5000,5000)
# tracer(0)
# m = 20

# for i in range(2):
#     forward(21*m); right(90);forward(27*m);right(90)
# up()
# forward(9*m)
# right(90)
# forward(10*m)
# left(90)
# down()
# for i in range(2):
#     forward(86*m); right(90); forward(47*m);right(90)

# up() # Обязательно не забываем поднять хвост!
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x*m, y*m)
#         dot(4,'red')
# done()

# №31352
# Повтори 5 [Вперёд 33 Направо 135 Вперёд 33 Направо 45].
# Найдите площадь фигуры. В ответе целое число.

# from turtle import *
# tracer(0)
# screensize(5000,5000)
# m = 20
#
# for i in range(5):
#     forward(33*m); right(135); forward(33*m); right(45)
#
# up() # Поднять хвост
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x * m, y * m)
#         dot(4,'green')
# done()
#print((1089 * 1.4142) / 2)







