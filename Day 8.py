c1="Make a lot of money" 
c2="buy now" 
c3="suscribe this" 
c4="click this"




c= input("Write a comment:")
(c==c1 or c==c2 or c==c3 or c==c4): 
if((c1 in c) or(c2 in c) or(c3 in c) or(c4 in c)):
    print("Spammer!")
else:
    print("thanks")
name= input("enter name:")
if(len(name)>=10):
    print("yes")
else:
    print("less then 10")
post= input("Enter a post:")
if("Harry".lower() in post.lower()):
    print("this post talking about harry")
