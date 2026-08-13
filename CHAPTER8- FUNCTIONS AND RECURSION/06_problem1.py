# Write a program using functions to find greatest of three numbers 
def greatest(a,b,c):
    if(a>b):
        return a
    elif(b>c):
        return b
    else:
        return c
a = int(input("enter value of a: "))
b = int(input("enter value of b: "))
c = int(input("enter value of c: "))
print(f"the greatest number is{greatest(a,b,c)} ")