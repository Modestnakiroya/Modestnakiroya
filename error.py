def main():
    print("Division Calculator")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    while True:
        try:
            num2 = float(input("Enter the second number (divisor): "))
            if num2 == 0:
                print("Error: Cannot divide by zero! Please enter a non-zero number.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    result = num1 / num2
    
    print(f"\nResult: {num1} ÷ {num2} = {result}")

if __name__ == "__main__":
    main()