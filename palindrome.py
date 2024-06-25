# https://python-reference.readthedocs.io/en/latest/docs/generator/

# Palindrome using generator

def reverse(string):
    for i in string[::-1]:
        yield i


def palindrome(string):
    rev_string = reverse(string)
    for i in string:
        if i != next(rev_string):
            return "Not palindrome"
    return "Palindrome"


print(palindrome('malayalam'))
