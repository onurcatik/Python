double = lambda x: x*2

print( double(2))
print( double(3))
print( double(4))

#  ---------------

add = lambda x,y: x+y
print(add(2,3))
print(add(4,5))


# -----------------

max_value = lambda x, y: x if x> y else y
print(max_value(2,3))
print(max_value(4,5))

#  ----------------

min_value = lambda x, y: x if x<y else y
print(min_value(6,1))
print(min_value(123123,1231))

#  -----------------

full_name = lambda first, last:  first + " " + last

print(full_name("SpongeBob", "AliMehemt"))

#  --------------

is_even = lambda x: x % 2 == 0

print(is_even(4))
print(is_even(25))

# ------------------

age_check = lambda age: True if age >= 18 else False

print(age_check(21))
print(age_check(17))