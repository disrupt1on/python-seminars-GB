recipe = {'Эспрессо': [1, 0, 0], 'Капучино': [1, 3, 0],
              'Маккиато': [2, 1, 0], 'Кофе по-венски': [1, 0, 2],
              'Латте Маккиато': [1, 2, 1], 'Кон Панна': [1, 0, 1]}
 
 
def choose_coffee(preferences):
    for i in preferences:
        if recipe[i][0] <= ingredients[0] and recipe[i][1] <= ingredients[1] and recipe[i][2] <= ingredients[2]:
            ingredients[0] -= recipe[i][0]
            ingredients[1] -= recipe[i][1]
            ingredients[2] -= recipe[i][2]
            return i
    return 'К сожалению, не можем предложить Вам напиток'

 
ingredients = [4, 4, 0]
print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))
print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))
print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))