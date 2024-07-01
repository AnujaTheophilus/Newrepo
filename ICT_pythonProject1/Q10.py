# Write a Python function to calculate the factorial of a number (a
# nonnegative integer). The function accepts the number as an argument.
# Sample input: 3 Sample output: 6
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    print(fact)

num = int(input('enter the number: '))
factorial(num)
