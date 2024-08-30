file = open("text.txt",'r')
counter = 0
content = file.read()
colist = content.split("\n")

for i in colist:
    counter +=1
print(counter)


x= open("file.txt","a")
y = x.write("Hello")
print(y)

x = open("text.txt","w")
x.write("Oops..! content deleted")
print(x)

import os
os.remove("thanuja.txt")
