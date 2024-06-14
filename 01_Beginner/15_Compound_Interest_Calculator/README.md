# Python Compound Interest Calculator

## Compound Interest Formula

The formula for calculating compound interest is:

\[ A = P \left(1 + \frac{r}{100}\right)^t \]

Where:
- \( A \) is the amount of money accumulated after n years, including interest.
- \( P \) is the principal amount (the initial amount of money).
- \( r \) is the annual interest rate (in percentage).
- \( t \) is the time the money is invested for (in years).

## Program Structure

1. **Input Validation**: Ensure that the user inputs valid values for the principal, rate, and time.
2. **Calculation**: Use the compound interest formula to compute the new balance.
3. **Output**: Display the new balance in a formatted manner.

## Step-by-Step Implementation

### 1. Input Validation

We will use a while loop to prompt the user for valid inputs. The input must be greater than zero for all three parameters (principal, rate, and time).

### 2. Calculation

We will use the formula mentioned above to calculate the new balance.

### 3. Output

The result will be displayed with two decimal places for clarity.

Here is the complete Python program:

```python
def get_valid_input(prompt, data_type=float):
    while True:
        try:
            value = data_type(input(prompt))
            if value <= 0:
                print(f"{data_type.__name__.capitalize()} cannot be less than or equal to zero. Please try again.")
            else:
                return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {data_type.__name__}.")

def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time

def main():
    print("Compound Interest Calculator")
    
    principal = get_valid_input("Enter the principal amount: ")
    rate = get_valid_input("Enter the interest rate: ")
    time = get_valid_input("Enter the time in years: ", int)
    
    total_balance = calculate_compound_interest(principal, rate, time)
    
    print(f"Balance after {time} years: ${total_balance:.2f}")

if __name__ == "__main__":
    main()
```

### Explanation

1. **Function `get_valid_input`**: This function ensures that the user inputs a valid number. It keeps prompting the user until a valid input greater than zero is provided.
    - **Parameters**:
        - `prompt`: The message displayed to the user.
        - `data_type`: The type of data expected (default is `float`).

2. **Function `calculate_compound_interest`**: This function computes the compound interest using the provided principal, rate, and time.
    - **Parameters**:
        - `principal`: The initial amount of money.
        - `rate`: The annual interest rate.
        - `time`: The time in years.

3. **Function `main`**: The main function of the program.
    - It prints a title.
    - It collects the principal, rate, and time from the user using `get_valid_input`.
    - It calculates the total balance using `calculate_compound_interest`.
    - It prints the result formatted to two decimal places.

## Testing the Program

Here are a few test cases to verify the program:

1. **Test Case 1**:
    - **Input**:
        - Principal: $1000
        - Rate: 10%
        - Time: 1 year
    - **Output**:
        - Balance after 1 year: $1100.00

2. **Test Case 2**:
    - **Input**:
        - Principal: $500
        - Rate: 7%
        - Time: 2 years
    - **Output**:
        - Balance after 2 years: $572.45

3. **Test Case 3**:
    - **Input**:
        - Principal: $1500
        - Rate: 5%
        - Time: 3 years
    - **Output**:
        - Balance after 3 years: $1738.13
.