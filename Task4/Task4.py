# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y)

n = int(input('Введите число четверти от 1 до 4 = '))
def possibleСoordinates(n):
    if (n == 1):
        print ("Диапазон возможных координат в 1 четверти x > 0 и y > 0")
    elif (n == 2):
        print ("Диапазон возможных координат во 2 четверти x < 0 и y > 0")
    elif (n == 3):
        print ("Диапазон возможных координат в 3 четверти плоскости x < 0 и y < 0")
    elif (n == 4):
        print ("Диапазон возможных координат в 4 четверти плоскости x > 0 и y < 0")
    else: 
        print ('Введите число четверти от 1 до 4 = ')
possibleСoordinates(n)