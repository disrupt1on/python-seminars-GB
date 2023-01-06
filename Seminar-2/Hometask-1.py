#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

realNumber = float(input("Введите число: "))

sum = 0
for i in str(realNumber):
    if i != ".":
        sum += int(i)

print(f"Сумма цифр равна = {sum}")

