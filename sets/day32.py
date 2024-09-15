s1={1,2,3}
s2={1,2,3,4,5,6,7}
#UNION() in SET
#UNION() does not changes s1 and s2
print(s1.union(s2))
#UPDATE() in SET
#It changes the value of s1
#s1.update(s2)
print(s1 , s2)

#INTERSECTION() in SET
#it does not change the values of s1 and s2
print(s1.intersection(s2))

#INTERSECTION_UPDATE() in SET
#it changes the values of s1 and s2
#s1.intersection_update(s2)

#SYMMETRIC_DIFFERENCE() in SET
print(s1.symmetric_difference(s2))

#DIFFERENCE() in SET
s3=s1.difference(s2)
print(s3,s1,s2)

#isdisjoin()
print(s1.isdisjoint(s2))
#issuperset()
print(s1.issuperset(s2))

#issubset()
print(s1.issubset(s2))

#add()
s1.add(4)

#remove()/discard()
#discard() does not throw an error
s1.discard(6)
#remove() throws an error if some value is not present
print(s1)
#pop()
#a random value gets popped as the set is unordered

#del is a keyword and it deletes the whole set
del s3

#clear empties the whole set
s3={1,2,3,4,5,6,7}
s3.clear()
print(s3)

#(in) in if
if 3 in s1:
    print("3 is present")
else:
    print("3 is not present")