## Write a program to find the largest of three numbers.
num1 = int(input("ENter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("ENter the third number: "))

if num1 > num2 and num1 > num3 :
    print(f"{num1} is the largest of the three numbers.")

elif num2 > num1 and num2 > num3:
    print(f"{num2} is the largest of the three numbers.")
    
else:
    print(f"{num3} is the largest of the three numbers.")
    