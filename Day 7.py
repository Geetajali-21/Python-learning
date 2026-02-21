a= int(input("enter a number:"))
if(a/10<3.3):
    print("fail")
b= int(input("enter a number:"))
if(b/10<3.3):
    print("fail")
c= int(input("enter a number:"))
if(c/10<3.3):
    print("fail")
d= int(input("enter a number:"))
if(a>b and a>c and a>d):
    print("a is greatest")

elif(b>a and b>c and b>d):
    print("b is greatest")

elif(c>a and c>b and c>d):
    print("c is greatest")

else:        #(d>a and d>c and d>b) 
    print("d is greatest")

total=a+b+c
per=total/3
if(a/10>3.3):
    print("fail")
elif(b/10>3.3):
    print("fail")
elif(c/10>3.3):
    print("fail")
total=a+b+c
per=total/3
print("percentage-",per,"%")

if(per>=33):
    print("Pass")
else:
    print("Fail")

