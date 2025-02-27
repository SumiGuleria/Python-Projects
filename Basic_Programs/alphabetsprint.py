## Given two char c1 and c2.  you need to print all the alphabet starting from c1 to c2, separated by space, in a single line.
c1 = input("Enter the starting alphabet. ")
c2 = input("Enter the last alphabet. ")
for  i in range(ord(c1),ord(c2)+1):
    print(" ".join(chr(i)))
    