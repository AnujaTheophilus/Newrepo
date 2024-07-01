#Write a Python program to check whether a number is prime or not.
# Sample input: Enter the number: 3
# Sample output: 3 is a prime number.

number = int(input('enter the number: '))
if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            print(number,'is not a prime number')
            break
    else:
        print(number,'is a prime number')
else:
    print(number,'is not a prime number')