# Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.
num = int(input("Enter an integer: "))
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3.")
elif num % 2 == 0:
    print("Divisible by 2.")
elif num % 3 == 0:
    print("Divisible by 3.")
else:
    print("Not divisible by 2 or 3.")