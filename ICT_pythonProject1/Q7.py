#  Write a Python program to find the sum of squares of the numbers in a
# list. Sample input: 2,1,3,1 Sample output: 15
sum = 0
numbers = input('enter the numbers: ').split(',')
for i in numbers:
    sum += int(i)**2
print(sum)