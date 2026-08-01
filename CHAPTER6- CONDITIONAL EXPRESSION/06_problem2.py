'''Write a program to find out whether a student has passed or failed if it require a total of 40% 
 and at least 33% in each subject to pass. Assume 3 subject and take marks as an input from the user'''

sub1 = int(input("enter marks of maths: "))
sub2 = int(input("enter marks of science: "))
sub3 = int(input("enter marks of english: "))

# check for total percentage 
total_percentage = (100)*(sub1 + sub2 + sub3)/ 300

if(total_percentage >=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("you are pass",total_percentage )

else:
    print("you are failed",total_percentage )

