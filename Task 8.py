# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

numberX = int(input('Введите координату Х '))
numberY = int(input('Введите координату Y '))

if numberX > 0 and numberY > 0:
    print('1 четверть')
elif numberX < 0 and numberY > 0:
    print('2 четверть')
elif numberX < 0 and numberY < 0:
    print('3 четверть')
elif numberX > 0 and numberY < 0:
    print('4 четверть')
elif numberX == 0 and numberY == 0:
    print('заданная точка находится в центре плоскости координат')    
elif numberX == 0:
    print('заданная точка находится на оси X')
elif numberY == 0:
    print('заданная точка находится на оси Y')