print("How many questions do you want to ask?")
n=int(input())
q=[i for i in range(1,n+1)]
a=[i for i in range(1,n+1)]
su=0
for x in range(n):
    print("Question is:-",q[x])
    an=int(input())
    if(an == a[x]):
       su+=1
print("Your score is:-",su)