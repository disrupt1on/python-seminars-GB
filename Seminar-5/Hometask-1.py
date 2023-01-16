#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст через пробел:\n")
print(f"Исходный текст: {text}")

searchWordsSet = "абв"
newText = [i for i in text.split() if searchWordsSet not in i]
print(f'Новый текст: {" ".join(newText)}')