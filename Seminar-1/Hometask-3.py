# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

coordX = int(input("Введите координату X: "))
coordY = int(input("Введите координату Y: "))

if coordX == 0 or coordY == 0:
    print("Введите координаты отличные от 0")
else:
    if coordX < 0 and coordY > 0:
        print("Точка находится в 1 четверти плоскости")
    elif coordX < 0 and coordY < 0:
        print("Точка находится во 2 четверти плоскости")
    elif coordX > 0 and coordY < 0:
        print("Точка находится в 3 четверти плоскости")
    elif coordX > 0 and coordY > 0:
        print("Точка находится в 4 четвети плоскости")