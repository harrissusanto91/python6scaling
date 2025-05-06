def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    else:
        print(f"The result is: {result}")

def main():
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    divide(num1, num2)

if __name__ == "__main__":
    main()
