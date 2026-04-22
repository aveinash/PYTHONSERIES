# A dictionary in Python is a collection of key–value pairs used to store data
# dict = {} empty dictionary if we add elements it become sets
marks = { "shiv":100 ,
         "rohan":200,
         "vishesh":23,
         0:"value"}


#methods
# print(marks.items())   
# print(marks.keys())
# print(marks.values())
print(marks.get("maths"))

marks.update({"shiv":90 , "avinash":89})
print(marks)