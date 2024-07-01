# Write a Python program to print only those numbers which are divisible
# of 5.
# Sample input: 10, 20,33,46,55 Sample output: 10, 20, 5


elements = input('enter the elements: ').split(',')
for i in elements:
    if int(i)%5 == 0:
        print(int(i))
