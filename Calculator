def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): 
    return "Error: Division by zero!" if y == 0 else x / y

def calculator():
    print("=== Calculator ===")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")

    while True:
        choice = input("\nSelect operation (1-5): ").strip()

        if choice == '5':
            print("Exiting calculator...")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select between 1 and 5.")

if __name__ == "__main__":
    calculator()
