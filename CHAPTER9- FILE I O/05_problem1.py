# write a program to read the text from a given file "poem.txt" and find out whetherit contain the word 'twinkle'

f= open("CHAPTER9- FILE I O/poem.txt")
content = f.read()

if("twinkle" in content):
    print("the word twinkle is present in content")
else:
    print("not present")
    
f.close()