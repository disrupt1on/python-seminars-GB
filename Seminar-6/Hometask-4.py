#Создайте список из случайных чисел. Найдите количество различных элементов в нем.

list1 = input("Введите список через пробел: ").split()
count = 0
list2 = []
for x in list1:
    if x not in list2:
        count += 1
        list2.append(x)
print(len(list2))