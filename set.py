s1={1,2,3}
s2={2,3}
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.symmetric_difference(s2))
s1.update(s2)
print(s1)


#convert list into set
l1=[1,2,3,4,5]
s1=set(l1)
print(s1)