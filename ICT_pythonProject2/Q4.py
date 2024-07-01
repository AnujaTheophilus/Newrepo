# Given a range of first 10 numbers, write a Python program to iterate from
# start number to the end number and print the sum of the current number
# and previous number.
# Sample input: 1….10
# Sample output: Current Number 1 Previous Number 0 Sum: 1 Current
# Number 2 Previous Number 1 Sum: 3 Current Number 3 Previous
# Number 2 Sum: 5… Current Number 10 Previous Number 9 Sum: 19

prev_num = 0
for current_num in range(1,11):
    sum = current_num + prev_num
    print(sum)
    prev_num = current_num
