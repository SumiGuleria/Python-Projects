## Calculate the factorial using Loops.
num = int(input("Enter the number you wish to have factorial of: "))
if num < 0 :
    print("The factorial cannot be derived for a negative number. ")
else:
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
        
    print(f"The factorial of {num} is {factorial}")