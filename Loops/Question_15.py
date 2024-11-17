# Print the sum of even and odd numbers separately up to a given number.
n = int(input("Enter a number: "))
sum_even, sum_odd = 0, 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
