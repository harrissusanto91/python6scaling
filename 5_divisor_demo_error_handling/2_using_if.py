def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = a / b
        print(f"The result is: {result}")

def main():
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    divide(num1, num2)

if __name__ == "__main__":
    main()
