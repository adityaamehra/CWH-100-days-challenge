# METHOD 1 TO ADD AN ELEMENT TO A TUPLE
coun=(1,2,3,4,5,6,7,8,9,10,3,3,3,3,3,3,3,3,3,33)
temp=list(coun)
temp.append(11)
coun=tuple(temp)
print(coun)
# COUNT METHOD 1
res=coun.count(3)
print(res)
# INDEX METHOD 
print(coun.index(3,3, len(coun)))
# METHOD 2 TO ADD AN ELEMENT TO A TUPLE
