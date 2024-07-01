# Write a Python program which iterates from 1 to 10. For multiples of 2,
# print “Fizz” instead of the number and for the multiples of 5, print “Buzz”.
# For numbers which are multiples of both 2 and 5, print “FizzBuzz”.
# Sample input: numbers from 1 to 10 Sample output: 1 Fizz 3 Fizz Buzz
# Fizz 7 Fizz 9 FizzBuzz

for i in range(1,11):
    if i % 2 ==0 and i % 5 == 0:
        print(i,'FizzBuzz')
    elif i % 2 == 0:
        print(i,'Fizz')
    elif i % 5 == 0:
        print(i,'Buzz')
    else:
        print(i)