n=int(input())
a=list(map(int,input().split()))
v=[]
for i in a:
    if i not in v:
        v.append(i)
        print(i,a.count(i),end=" ")