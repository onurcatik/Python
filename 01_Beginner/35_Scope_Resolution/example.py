def function_one():
    a=1
    print(a)

def function_two():
    b=2
    print(b)
function_one()
function_two()

# ---------------------
e=3
def outer_function():
    x=1

    def inner_function():
        print(x)

    inner_function()

def function_with_built_in():
    from math import e 
    print(e)

outer_function()
function_with_built_in()
print(e)


# ---------------------

def outer_function():
    x=1
    def inner_function():
        print(x)
    inner_function()

outer_function()



 