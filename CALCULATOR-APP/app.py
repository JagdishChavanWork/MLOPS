from calc_function import do_addition, do_subtraction
def main():
    print("Welcome to the calculator app!")
    print("""\nselect the function from the given option:
            1. Addition
            2. Subtraction
        """)
    

    user_input = input("Select the function")

    a = int(input("Value of A: "))
    b = int(input("Value of B: "))

    if user_input == "1":
        result =  do_addition(a, b)
    
    elif user_input == "2":
        result = do_subtraction(a, b)

    print("Result: ", result)


if __name__ == "__main__":
    main()