n=int(input())
a=list(map(int,input().strip().split()))[:n]
s=0
v=list(set(a))
for i in range(0,len(v)):
    if v[i]==a.count(v[i]):
        s=s+1
print(s)
