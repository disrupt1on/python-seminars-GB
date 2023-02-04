#Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Найдите самого младшего из друзей и выведите его имя.

n = int(input('Введите кол-во словарей: '))

friends = {}

for i in range(n):
    name = input('Введите имя друга: ')
    age = int(input('Введите возраст друга: '))
    friends[name] = age

list_of_friends = list(friends.items())
print('Список друзей:', friends)

min_age = min(friends.values())
for name, age in friends.items():
        if age == min_age:
            print('Самый младший из друзей:', name)
