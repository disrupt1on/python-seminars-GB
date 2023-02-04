# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Выведите средний возраст всех друзей и самое длинное имя.

n = int(input('Введите количество друзей: '))
friends = {}

for i in range(friends):
    name = input('Введите имя: ')
    age = int(input('Введите возраст: '))
    friends[name] = age

friends_list = list(friends.items())
print('Список друзей:', friends)

count = 0
for name, age in friends.items():
    count += age
count /= friends
print('Средний возраст всех друзей = ', count)

longest_name = max(friends, key = len)
for name, age in friends.items():
        if len(name) == len(longest_name):
            print('Самое длинное имя - ', name)