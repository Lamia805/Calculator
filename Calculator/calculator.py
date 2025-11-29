# Create Arithmetic Functions
def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1,num2):
    if num2==0:
        return "Error: Divion by zero not allowed"
    return num1/num2

#  User Input & Displaying Results
num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))

print("The addition result:", add(num1,num2))
print("TThe subtraction result:", subtract(num1,num2))
print("The multiplication result:", multiply(num1,num2))
print("The division result :", divide(num1,num2))

#  Input Validation

def get_valid_number(prompt):
    while True:
        user_input=input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input please enter the numeric value")

# Menu-Based Calculator

print("--- My Calculator ---")

while True:
    print("\nSelect Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting calculator, Please Use me Again!!")
        break

    if choice in ('1', '2', '3', '4'):
        n1 = get_valid_number("Enter first number: ")
        n2 = get_valid_number("Enter second number: ")

        if choice == '1':
            print(f"{n1} + {n2} = {add(n1, n2)}")
        elif choice == '2':
            print(f"{n1} - {n2} = {subtract(n1, n2)}")
        elif choice == '3':
            print(f"{n1} * {n2} = {multiply(n1, n2)}")
        elif choice == '4':
            result = divide(n1, n2)
            if result == "Error: Division by Zero":
                print(result)
            else:
                print(f"{n1} / {n2} = {result}")
    else:
        print("Invalid choice, please try again.")


# Convert to Object-Oriented Calculator
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by Zero"
        return a / b

    def get_valid_number(self, prompt):
        while True:
            user_input = input(prompt)
            try:
                return float(user_input)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

    def menu(self):
        print("OOP Calculator Menu ...")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

    def run(self):
        print("Starting Calculator...")
        
        while True:
            self.menu()
            choice = input("Enter choice (1-5): ")

            if choice == '5':
                print("Exiting calculator, Please Use me Again!!")
                break

            if choice in ('1', '2', '3', '4'):
                n1 = self.get_valid_number("Enter first number: ")
                n2 = self.get_valid_number("Enter second number: ")

                if choice == '1':
                    print(f"Result: {n1} + {n2} = {self.add(n1, n2)}")
                elif choice == '2':
                    print(f"Result: {n1} - {n2} = {self.subtract(n1, n2)}")
                elif choice == '3':
                    print(f"Result: {n1} * {n2} = {self.multiply(n1, n2)}")
                elif choice == '4':
                    result = self.divide(n1, n2)
                    if result == "Error: Division by Zero":
                        print(result)
                    else:
                        print(f"Result: {n1} / {n2} = {result}")
            else:
                print("Invalid Input. Please select 1, 2, 3, 4, or 5")


if __name__ == "__main__":
    calc_app = Calculator()
    calc_app.run()


