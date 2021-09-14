fruits = ["Lemon", "Apple", "Pineapple"]

def add_fruit(fruits, fruit_to_add):
    fruits.append(fruit_to_add)
    print('Fruits inside function', fruits)

fruit_to_add = input("Add fruit you love:")
add_fruit(fruits, fruit_to_add)
print('Fruits outside function', fruits)