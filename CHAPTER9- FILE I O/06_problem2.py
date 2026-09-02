'''write a program to generate multiplication tables
from 2 to 20 and writw it to the different files place these files
in a folder for  a 13 year old'''
import os

def generateTable(n):
    tables = ""

    for i in range(1, 11):
        tables += f"{n} X {i} = {n * i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(tables)



os.makedirs("tables", exist_ok=True)

for i in range(2, 21):
    generateTable(i)