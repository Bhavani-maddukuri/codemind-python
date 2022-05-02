n=int(input())
a=list(map(int,input().strip().split()))[:n]
s=int(input())
v=list(set(a))
d=0
for i in range(0,len(v)):
    if s==a.count(v[i]):
        print(v[i],end=" ")
        d=1
if d==0:
  print(-1)


