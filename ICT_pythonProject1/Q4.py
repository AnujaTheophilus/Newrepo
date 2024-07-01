# Write a Python function that takes a positive integer and returns the sum
# of the cube of all the positive integers smaller than the specified number.
# Sample input: 4 Sample output: 36.

def sum_cube(n):
    sum = 0
    for i in range(1,n):
        sum += i**3
    print(sum)
n = int(input('enter the number'))
sum_cube(n)