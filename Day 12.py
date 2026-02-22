n= int(input("enter a number:"))
i=0
for n in range(n,i):
    if(i%2==0):
        print(i,"even number")
        print(n,"x",i,"=",i*n)
        print(""*(n-i),end="")
        print("+"*(2*i+1),end="")
        print("\n")
        print(i)
