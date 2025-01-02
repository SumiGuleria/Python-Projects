# Write a program to check if a string is a palindrome or not.

str= input("Enter the string you wish to check is palindorme or not:  ")
if str.lower()== str[::-1].lower():
    print(f"The string {str} is palindrome.")
else:
    print("The string is not palindorme.")