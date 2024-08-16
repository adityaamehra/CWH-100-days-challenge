l=[3,5,6,"hello world",True,0.000000006]
print(l)
print(type(l))

for i in l:
    print(i,end=" ")
print()
#negative indexing
print(l[-3])
#IN KEYWORD
if "hello world" in l:
    print("YES")
else:
    print("NO")

if "ditya" in "Adityaa Mehra":
    print("YES")

#JUMP INDEX IN LIST

print(l[::2]) #THE 2 HERE SIGNIFIES THAT IT IS GOING TO SKIP SOME ELEMENTS and it is the jump index

#LIST COMPREHENSION
lst= [i**i for i in range(10) if i%2 ==0]
print(lst)