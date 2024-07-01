# Write a Python program to find the maximum of three numbers
# Sample input: 34,12,7
# Sample output: 34

num1 = int(input('enter the number: '))
num2 = int(input('enter the number: '))
num3 = int(input('enter the number: '))
if num1 > num2 and num1 > num3:
    print(num1,'is the largest number')
elif num2 > num1 and num2 > num3:
    print(num2,'is the largest number')
else:
    print(num3,'is the largest number')