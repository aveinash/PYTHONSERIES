# write the program to find whether a given username contains less than 10 character or not 

username = input("enter username: ")
if(len(username)<=10):
    print("username contain less than 10 character")

else:
    print("more than 10")