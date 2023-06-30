print("Calculator by Khodchenkov \n")

try:
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()


operator = input("Please select an operation: (\n 1. Addition, \n 2. Subtraction, \n 3. Multiplication, \n 4. Division \n Enter your choice (1-4): ")


def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y 
def multiplication (x,y):
    if x == 0 or y == 0:
        return 0
    else:
        return x * y
def Division (x,y):
    if x == 0 or y == 0:
        return 0
    else:
        return x / y


if operator in ["1", "2", "3", "4"]:
    if operator == "1":
        result = addition (num1, num2)
    elif operator == "2":
        result = subtraction (num1, num2)
    elif operator == "3":
        result = multiplication (num1, num2)
    elif operator == "4": 
        result = Division (num1, num2)

else:
    print("Invalid operator. Please enter a valid operator (1-4)")
    exit()

print ("The result of multiplication is: ", result )