print("Calculator by Khodchenkov \n")

num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
operator = input("Please select an operation: (\n 1. Addition, \n 2. Subtraction, \n 3. Multiplication, \n 4. Division \n Enter your choice (1-4): ")


def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y 

def multiplication (x,y):
    return x * y

def Division (x,y):
    return x / y

if operator == "1":
    result = addition (num1, num2)
elif operator == "2":
    result = subtraction (num1, num2)
elif operator == "3":
    if num1 == 0 or num2 == 0:
        print("Error: Multiplication by zero is not allowed.")
    else:
        result = multiplication (num1, num2)
elif operator == "4":
    if num1 == 0 or num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = Division (num1, num2)
else:
    print("Incorrect operator")

print ("The result of multiplication is: ", result )