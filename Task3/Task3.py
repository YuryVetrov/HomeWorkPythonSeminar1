# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
#Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x = int(input('Введите число не равное 0, где Х = '))
y = int(input('Введите число не равное 0, где Y = '))
def sector(x, y):
    if (x > 0 and y > 0):
        print ("Лежит в 1 четверти плоскости")
    elif (x < 0 and y > 0):
        print ("Лежит во 2 четверти плоскости")
    elif (x < 0 and y < 0):
        print ("Лежит в 3 четверти плоскости")
    elif (x > 0 and y < 0):
        print ("Лежит в 4 четверти плоскости")
sector(x, y)