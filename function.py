
#____________Python function____________

def fun():
  print("Hello")
fun()
fun()

def add(x,y):
    z=x+y
    return z

x,y=5,10
ans=add(x,y)
print('addition is:',ans)


x = lambda a, b : a * b
print("multiplication is:")
print(x(5, 6))

