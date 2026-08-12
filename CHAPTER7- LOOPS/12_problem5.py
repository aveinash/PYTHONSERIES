# write a program to calculate the factorial of a given number using for loop
# 5!= 1 x 2 x 3 x 4 x 5 
n = int(input("enter the number: "))
product = 1
for i in range(1,n+1):
    product = product * i
print("the factorial of given number",n ,"is",product) # thats why we use f string to avoid that so many comas
