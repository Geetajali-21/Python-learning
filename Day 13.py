COMPARISION BTW THREE NUM
a=2
b=6
c=4


def comp():
    if(a>b and a>c):
        print("a is gretest")
    elif(b>c and b>a):
        print("b is gretest")
    else:
        print(" c is greatest")

comp()
comp()


CELCIUS TO FAHRENHITE
c = int(input("enter  celsius :"))
def far():
    farenhite =  ( c*1.8)+32
    print(farenhite)

far() 

SUM OF N NUMBER
n = int ( input("enter a number"))

def sum():
    i=1
    s=0
    for i in range (i,n+1):
        s= s+i
    print(s)
sum()       


def pattern(n):
    if (n==0):
        return
    # print(""*(n-1))
    print("*" * n)
    # print("\n")
    pattern(n-1)

pattern(8)


INCHES TO CM
def inches(n):
    # cm= 2.54*n
    # print(cm)
    return n*2.54

# inches(6)
n= int(input("enter inches :"))
print(f"{inches(n)}")
