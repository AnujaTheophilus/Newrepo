# Write a Python program using for loop that will iterate from 1 to 15. For
# each iteration, check if the current number is odd or even, and display the
# message to the screen as odd or even. Sample input: 1….15 Sample
# output: 1-odd 2-even …. 15-odd

for i in range(1,16):
    if i % 2 == 0:
        print(i,'-even')
    else:
        print(i,'-odd')