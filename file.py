
#___with for loop
file=open('file1.txt','r')
for a in file:
    print(a)

#____read()
file=open("file1.txt","r")
print(file.read())

#_____with statement
with open("file1.txt")as file:
    data=file.read()
print(data)
 
#_____to read certain no of character
file=open ("file1.txt",'r')
print(file.read(2))
