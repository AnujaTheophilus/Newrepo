#  Write a Python program to find the most frequent item in a list of
# numbers. Sample input: 2, 3, 4, 2, 5, 2 Sample output: 2
list_numbers = []
numbers = input('enter the numbers:').split(',')
for i in numbers:
    list_numbers.append(i)
print(max(list_numbers, key=list_numbers.count))
