operator = input("Enter an operator (+, -, *, /): ")

num1 = float(input("First Number:"))
num2 = float(input("Second Number"))

if operator == "+":
    result=round(num1 + num2, 3)
elif operator == "-":
    result = round(num1 - num2, 3)
elif operator == "*":
    result = round(num1 * num2, 3)
elif operator == "/":
    result =round(num1 / num2 , 3)
    if num2 != 0:
       result (round(num1 / num2, 3)) 
    else:
        result = "Undefined"
else:
    result= "invalid operator"

print("Result is", result)