# Write a Python function called exponent(base,exp) that returns an
# integer value of base raises to the power of exp. Sample input: Enter the
# base: 2 Enter the exponent: 3 Sample output: 8

def exponent(base,exp):
    output = base ** exp
    print(output)

base = int(input('enter the base number: '))
exp = int(input('enter the exponent number: '))
exponent(base,exp)