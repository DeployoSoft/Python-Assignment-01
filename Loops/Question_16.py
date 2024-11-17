# Create a program to calculate the sum of the digits of an inputted integer.
num = int(input("Enter an integer: "))
total = 0
while num != 0:
    total += num % 10
    num //= 10
print("Sum of digits:", total)
