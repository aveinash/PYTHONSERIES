#A function is a block of code that performs a specific task. Instead of writing the same code again and again, 
# we write it once inside a function and call it whenever we need it.

def avg():  #function definition

    a = int(input("enter value of a: "))
    b = int(input("enter value of b: "))
    c = int(input("enter value of c: "))
    average = (a+b+c)/3
    print(average)
    
avg() # function call

avg()
