fruits = ["banana", "orange", "apple", "coconut"]
print(fruits)

fruits.sort()
print(fruits)

# ----------------

sorted_fruits = sorted(fruits)
print(sorted_fruits)

# ----------------

fruits.sort(reverse=True)
print(fruits)

# -----------------

fruits_tuple = ("banana", "orange", "apple", "coconut")
print(fruits_tuple)

# ------------------

fruits_dict = {
    "banana": 105,
    "orange": 73,
    "apple": 72,
    "coconut": 354
}
print(fruits_dict)

sorted_fruits_dict = dict(sorted(fruits_dict.items()))
print(sorted_fruits_dict)

# -------------------

sorted_by_values = dict(sorted(fruits_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)

#  ----------------

class Fruits:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name}: {self.calories} calories"
    
fruits = [
    Fruits("banana", 105),
    Fruits("apple", 72),
    Fruits("orange", 73),
    Fruits("coconut", 354)
]
print(fruits)

sorted_fruits = sorted(fruits, key=lambda fruit: fruit.name)
print(sorted_fruits)

sorted_by_calories = sorted(fruits, key=lambda fruit: fruit.calories)
print(sorted_by_calories)

sorted_by_calories_desc = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)
print(sorted_by_calories_desc)