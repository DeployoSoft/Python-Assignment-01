# Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == '+':
    print(a + b)
elif operator == '-':
    print(a - b)
elif operator == '*':
    print(a * b)
elif operator == '/':
    print(a / b if b != 0 else "Division by zero is not allowed.")
else:
    print("Invalid operator.")
