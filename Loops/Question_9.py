# Write a program to print the first 10 Fibonacci numbers.
a, b = 0, 1
print(a, b, end=" ")
for _ in range(8):
    a, b = b, a + b
    print(b, end=" ")
