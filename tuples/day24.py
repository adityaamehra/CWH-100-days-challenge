tup = (1,2,3,3,4,5,6,7,78,8,9,9,90)
# print(type(tup))
# print(tup)
for x in tup:
    print(x,end=' ')
print()
if 8 in tup:
    print(True)
else:
    print(False)
tup2=tup[2:5]
print(tup2)