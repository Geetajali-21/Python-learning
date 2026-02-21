s = {1,2,3,4,5,6,"harry"}
print(s,type(s))
s.add(566)
print(s,type(s))


set1={1,34,23,45,6}
set2={33,43,2,31,34}
set1.add(7)
print(set1)
print(set1.difference(set2))
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.issuperset({1,34}))
print({1,34}.issubset(set1))
print(set1.pop())
set1.clear()
print(set1)
words={
    "cat":"billi",
     "help":"madad",
    "cow": "gaay"

}
word=input("enter the word you want  maeaning of :")
print(words[word])

s=set()
n= input("enter number")
s.add(n)
n= input("enter number")
s.add(n)
n= input("enter number")
s.add(n)
n= input("enter number")
s.add(n)
n= input("enter number")
s.add(n)
n= input("enter number")
s.add(n)
n= input("enter number")
s.add(n)
n= input("enter number")
s.add(n)
n= input("enter number")
s.add(n)
print(s)

