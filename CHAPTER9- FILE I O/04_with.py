f = open("CHAPTER9- FILE I O/file.txt")
print(f.read())
f.close()

# the same can be written using with statement like this:
with open("CHAPTER9- FILE I O/file.txt") as f:
    print(f.read())

# you dont have to explicitly close the file 