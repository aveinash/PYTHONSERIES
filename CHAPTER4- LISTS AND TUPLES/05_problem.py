# write a program to accept marks of 5 students and display them in a sorted manner 

marks = []
s1 = int(input("enter marks of student 1: "))
marks.append(s1)
s2 = int(input("enter marks of student 2: "))
marks.append(s2)
s3 = int(input("enter marks of student 3: "))
marks.append(s3)
s4 = int(input("enter marks of student 4: "))
marks.append(s4)
s5 = int(input("enter marks of student 5: "))
marks.append(s5)

marks.sort()
print(marks)