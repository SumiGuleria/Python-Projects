'''Given a string s, you need to perform the following operation.

1. Capitalize the first letter and print.

2. Convert the whole string to uppercase and print.'''

s = input("Enter the string. ")
print(s.upper())
for i in range(0, len(s)+1):
    if i == 0:
        print(s[i].upper(), end='')
    else:
        print(s[i], end='')