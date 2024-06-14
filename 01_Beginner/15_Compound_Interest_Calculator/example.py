def get_valid_input(prompt, data_type=float)
    while True:
        try:
            value = data_type(input(prompt))
            if value <= 0:
                print(f"{data_type.__name__.capitalize()} cannot be less than or dqual to zero . Please try again.")
                else
                return value
        except ValueError:
            print(f"Invalid Input {data_type.__name__}")
def calculate_compound_interest(principial, rate, time):
    return principial*(1+ rate/ 100) ** time
def main():
    print("Compound Interest Calculator")

    principal = get_valid_input("Enter the principal amount: ")
    rate = get_valid_input("Enter the interest rate: ")
    time = get_valid_input("Enter the time in years: ", int)
    
    total_balance = calculate_compound_interest(principal, rate, time)
    
    print(f"Balance after {time} years: ${total_balance:.2f}")

if __name__ == "__main__":
    main()