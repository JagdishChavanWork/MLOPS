from calc_function import do_addition, do_subtraction, do_division
from multiply import do_multiplication
from area import calculate_area_rectangle
def main():
    print("Welcome to the calculator app!")
    print("""\nselect the function from the given option:
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
        """)
    

    user_input = input("Select the function")

    a = int(input("Value of A: "))
    b = int(input("Value of B: "))

    if user_input == "1":
        result =  do_addition(a, b)
    
    elif user_input == "2":
        result = do_subtraction(a, b)
    
    elif user_input == "3":
        result = do_multiplication(a, b)

    elif user_input == "4":
        result = do_division(a, b)

    print("Result: ", result)

    
    


if __name__ == "__main__":
    main()