# Write a Python program to construct the following pattern, using a
# nested for loop.
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
n = int(input('enter the range: '))
for i in range(1,n):
    for j in range(1,i+1):
        print('*',end = '')
    print('')
for k in range(n,0,-1):
    for _ in range(k):
        print('*',end = '')
    print('')