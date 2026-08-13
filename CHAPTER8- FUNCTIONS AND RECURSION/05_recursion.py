# Recursion is a function which calls itself 
# it is used to directly use a mathematical formula as function 

# factorial using recursion
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)
n = int(input("enter the number: "))
factorial(n)
print(f"the factorial of this number is: {factorial(n)}")


