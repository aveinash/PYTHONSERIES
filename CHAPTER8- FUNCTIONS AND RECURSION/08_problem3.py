# write a recursive function to calculate the sum of first n natural numbers 
def sum(n):
    if(n==0 ):
        return 0
    if(n==1):
        return 1
    else:
        return n + sum(n-1)
n = int(input("enter the natural numbers"))
print(f"the sum is: {sum(n)}")
    