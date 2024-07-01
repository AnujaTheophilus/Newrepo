# Write a Python program to accept a string value from the user and display
# the count of each character in that string. Sample input: Enter a string
# value: assembly Sample output: a=1, s=2, e=1, m=1, b=1, l=1, y=1

character_count = {}
string = input('enter the string: ')
for i in string:
    if i in character_count:
        character_count[i] += 1
    else:
        character_count[i] = 1
for char,count in character_count.items():
    print(char,'=',count,end = ',')

