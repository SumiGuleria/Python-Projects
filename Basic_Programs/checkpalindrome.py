# WAP to check whether a number is palindrome or not
n = 101
#if n == n[::-1]
a = str(n)
print(a[::-1])
if n == int(a[::-1]):
    print("True")
else:
    print("False")
