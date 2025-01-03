# Write a program to check if a number is prime or not.
# A number is prime if it is only divisible by one and itself.
num = int(input("ENter the number you wish to check: "))
if num <= 1:
    print(f"{num} is not a prime number. ")
    
else:
    is_prime = True #flag variable
    
    # Check divisibility from 2 to square root of num
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
        
    if is_prime:
        print(f"{num} is a prime number. ")
        
    else:
        print(f"{num} is not a prime number. ")
    