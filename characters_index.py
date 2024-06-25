# WAP to print char with their index.
s = input("Enter the string")
d = dict()
for char in s:
    print(char,s.index(char))
    d[char] = s.index(char)
print(d)
