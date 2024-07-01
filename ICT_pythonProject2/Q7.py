# Write a Python program to reverse a list using for loop.
# Sample input: 10,40,30,70
# Sample output: 70,30,40,10


elements = input('enter the elements: ').split(',')
for i in elements[::-1]:


    print(i,end = ',')
