# write a python function to print multiplication table of a given number 
 
def Mul(n):
    for i in range(1,11):
        print(i*n)
n = int(input("enter the number: "))
print(Mul(n))

