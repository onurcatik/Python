fruits =["apple", "orange",   "banana" , "coconut"]

print(fruits[0])
print(fruits[3])

# ---------

fruits [0] ="pineapple"
print(fruits)
# ---------


fruits.append("pineapple")
print(fruits)
# ---------


fruits.remove("pineapple")
print(fruits)

# ---------

for fruit in fruits:
    print(fruit)

# ---------

print(len(fruits))

# ---------

fruits.reverse()
print(fruits)

# ---------
print(fruits.count("banana"))

# ---------

print("apple" in fruits)
print("pineapple" in fruits)

