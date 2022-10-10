# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

number_quarter = int(input('Введите номер четверти '))
if number_quarter == 1:
    print ('X > 0, Y > 0')
elif number_quarter == 2:
    print ('X < 0, Y > 0')
elif number_quarter == 3:
    print ('X < 0, Y < 0')
elif number_quarter == 4:
    print ('X > 0, Y < 0')
else:
    print ('Число равно 0 или больше 4')