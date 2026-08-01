# write a program which finds out whether a given name is present in a list or not 

l = ["rohan","shubham","rohit","navya"]
name = input("Enter the name: ")

if(name in l):
    print("the name is on the list")
else:
    print("the name is not in the list")