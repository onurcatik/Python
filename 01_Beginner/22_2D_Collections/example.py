fruits = ["apple" , "orange" , "banana" , "coconut"]
vegetables = ["celery" , "carrots" , "potatoes"]
meats = ["chicken" , "fish" , "turkey"]

groceries = [fruits , vegetables, meats]

print(groceries)


print(groceries[0][0])
print(groceries[1][2])
print(groceries[2][2])


# -----------

numpad = (
    (1,2,3),
    (4,5,6),
    (7,8,9),
    ('*',0,'#')
)

print(numpad)


for row in numpad :

    for num in row:
        print(num, end=' ')
    print()