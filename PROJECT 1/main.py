import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([1,-1,0])
yourstr = input("enter your choice: ")
yourDict = {"s":1,"w":-1,"g":0}
reverseDict = {1: "Snake",-1:"Water",0:"Gun"}
you = yourDict[yourstr]
print(f"you choose{reverseDict[you]}\ncomputer choose {reverseDict[computer]}")


if(computer == you):
    print("its a draw")
else:
    if(computer == -1 and you == 1):
        print("you win")

    elif(computer == -1 and you == 0):
        print("you lose")

    elif(computer == 1 and you == -1 ):
        print("you lose")

    elif(computer == 1 and you == 0 ):
            print("you win")

    elif(computer == 0 and you == -1 ):
            print("you win")

    elif(computer == 0 and you == 1 ):
            print("you lose")
    else:
          print("something went wrong")