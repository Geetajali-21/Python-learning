comp= random.randint(1,100)
attempt=0
max_attempt=5
while attempt<max_attempt:
    you= int(input("enter a num  b/w 1-100"))
    attempt+=1
    if (you>comp):
        print("too high")
    elif(you<comp):
        print("too low")
    elif(you==comp):
        print("you win!")
    else:
        print("something wrong")
        break
    if(attempt==max_attempt and comp!=you):
        print("Game over !",comp)
