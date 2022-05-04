n=int(input())
a=list(map(int,input().split()))
v=[]
s=0
for i in a:
    if i not in v and i%2==0:
        v.append(i)
        
print(len(v))