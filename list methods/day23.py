l=[i+1 for i in range(6)]
print(l)
#APPEND FUNCTION 
l.append(7)
print(l)
#SORT FUNCTION
l.sort()
print(l)
l.sort(reverse=True)
print(l)
#REVERSE FUNCTION
l.reverse()
print(l)
#index FUNCTION
print(l.index(3))
#COPY FUNCTION
m=l.copy()
m[0]=0
print(m)
#INSERT FUNCTION
l.insert(1,899) #899 ki index list me 1 hogi
#EXTEND FUNCTION
m=[68,69,343243253]
l.extend(m)
print(l)
#CONCATINATION
k=l+m
print(k)