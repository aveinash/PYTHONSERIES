# write a python function which converts inches to cms 
def Convert(n):
    if(n==0):
        return 0
    else:
        return n * 2.54 
n = int(input("enter value in inches: "))
print(Convert(n))
