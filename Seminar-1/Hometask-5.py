# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

coordX, coordY = int(input("Введите координату X: ")), int(input("Введите координату Y: "))
coordX2, coordY2 = int(input("Введите координату X2: ")), int(input("Введите координату Y2: "))

KL = coordY - coordY2
ML = coordX2 - coordX

print(round((KL ** 2 + ML ** 2) ** 0.5, 2))