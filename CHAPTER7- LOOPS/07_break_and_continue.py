# break is used to exit the loop now
for i in range(1,100):
    if(i==33):
        break  #exit the loop right now
    print(i)

# continue is used to skip the iteration and continue with next one
for i in range(1,100):
    if(i==33):
        continue  #skip the iteration
    print(i)


# ex
for i in range(4):
    print("printing")
    if i==2:
        continue
    print(i)
