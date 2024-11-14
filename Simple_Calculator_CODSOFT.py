def calculator():
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/) ")
    print("5. Modulus (%)")
    print("6. Percentage (%)")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif choice == '5':
        result = num1 % num2
    elif choice == '6':
        result = (num1 / num2) * 100 if num2 != 0 else "Error: Division by zero"
    else:
        return "Invalid choice."

    return f"Calculated Result: {result}"
print(calculator())

