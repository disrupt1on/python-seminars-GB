#Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму

N = int(input("Введите число N: "))

list = [round((1 + 1 / i) ** i, 3) for i in range(1, N + 1)]

print(f'Для N = {N}: {list} Сумма: {round(sum(list), 3)}')