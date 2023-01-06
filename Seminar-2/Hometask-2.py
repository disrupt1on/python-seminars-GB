numberN = int(input("Введите число: "))

def numbersMult(n):
    if n == 1:
        return 1
    else:
        return n * numbersMult(n - 1)


list = []

for i in range (1, numberN + 1):
    list.append(numbersMult(i))

print(f"Пусть N = {numberN}, тогда произведения чисел от 1 до {numberN} - {list}")
