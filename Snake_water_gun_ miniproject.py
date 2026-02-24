import random


com= random.choice([0,1,-1])
you = input("Enter a word among them W or S or G: ")
youstr= {"s": -1, "w": 1,"g":0}
item={ -1:"snake",1:"water",0:"gun" }
you=youstr[you]
print(f"you choose {item[you]}\n computer choose {item[com]}")
if(you==com):
    print("draw game")
else:
    if( com==1 and you==-1):
       print("WIN !")
    elif( com==-1 and you==1):
      print("lose")
    elif( com==0 and you==1):
       print("WIN !")
    elif( com==-1 and you== 0):
        print("WIN !")
    elif( com==1 and you==0):
        print("lose !")
    elif( com==0 and you== -1):
        print("lose!")
    else:
        print("somthing went wrong")

