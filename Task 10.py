# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

numberX1 = int(input('Введите координату Х1: '))
numberY1 = int(input('Введите координату Y1: '))
numberX2 = int(input('Введите координату Х2: '))
numberY2 = int(input('Введите координату Y2: '))
import math
distance_between_points = math.sqrt(pow(numberX2-numberX1, 2) + pow(numberY2-numberY1, 2))
print(f'Расстояние между точками {round(distance_between_points, 2)}')