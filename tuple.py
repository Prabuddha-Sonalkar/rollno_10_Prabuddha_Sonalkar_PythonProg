fruits = ("apple", "banana", "cherry","watermelon","mango")
print(len(fruits))

tuple1 = ()
print(tuple1)

tuple1 = (1, 2, 3)
print(tuple1)

tuple1 = (1, "Hello", 3.4)
print(tuple1)

tuple1 = ("mouse", [8, 4, 6], (1, 2, 3))
print(tuple1)
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")

print(letters[0])   # prints "p" 
print(letters[5])   # prints "a"

print(letters[-1])   # prints 'z' 
print(letters[-3])   # prints 'm'

# elements 2nd to 4th index
print(tuple1[1:4])  #  prints ('r', 'o', 'g')

# elements beginning to 2nd
print(tuple1[:-7]) # prints ('p', 'r')

# elements 8th to end
print(tuple1[7:]) # prints ('i', 'z')

# elements beginning to end
print(tuple1[:]) # Prints ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')