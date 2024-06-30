try:
    number = int(input("Enter a number:"))
    result = 1 / number
    print(result)

except ZeroDivisionError:
    print("Your cannot.")
except ValueError:
    print("You must enter a number.")

#  -------------------------

try : 
    number=int(input("Enter a number: "))
    result = 1 / number
    print(result)
except ZeroDivisionError:
    print("Your cannot.")
except ValueError:
    print("You must enter a number.")
except Exception as e : 
    print(f"An unexpected: {e}")

#  -------------------------


try:
    number = int(input("Enter a number: "))
    result = 1 / number
    print(result)
except Exception as e:
    print(f"An unexpected error occurred: {e}")


#  -------------------------

