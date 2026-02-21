
n=int(input("enter a number:"))
i=0
for i in range(i,n+1):
    print("",end="")
    print("*"*i,end="")
    print("")
def greet(name,ending):
    print("Good morning"+ name,ending)
    return "done"

a=greet(" geetanjli", "thaniks")
b=greet(" sabiya","thanks")
print(a)
