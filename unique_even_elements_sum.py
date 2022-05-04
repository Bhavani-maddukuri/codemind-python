n=int(input())
a=list(map(int,input().split()))
v=[]
s=0
for i in a:
    if i not in v:
        v.append(i)
        if i%2==0:
            s=s+i
print(s)          
        