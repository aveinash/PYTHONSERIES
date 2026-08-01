''' write a program to find the greatest of four numbers entered by user'''
a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
c = int(input("enter number 3: "))
d = int(input("enter number 4: "))

if(a>b and a>c and a>d):
    print("greatest number is: ",a)
elif(b>a and b>c and b>d):
    print("greatest number is: ",b)
elif(c>a and c>b and c>d):
    print("greatest number is: ",c)
else:
    print("greatest number is: ",d)

