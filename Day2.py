a = '''geetanjli'''
ashort = a[0:4]
b = 'my name is "geetanjali"  gupta'
print(len(a))
print(ashort)
print(a[-6])
print(a[:9])
print(a[0:])
print(a[0:7:2])
print(a.endswith("li"))
print(a.startswith("e"))
print(a.capitalize())
print(b)

name = input("enter your name: ")
print(f"good morning {name}")
letter = '''Dear <|name|>," \
          You are selected 
          <|Date|>'''
print(letter.replace("<|name|>","Geetanjli").replace("<|Date|>","21 jan"))
name="may name is   geetqanjali gupta"
print(name.find("g"))
print(name.replace("  "," "))
