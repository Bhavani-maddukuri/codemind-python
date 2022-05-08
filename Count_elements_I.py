n,m=map(int,input().split())
n1=list(map(int,input().split()))
m1=list(map(int,input().split()))
s=0
n1=list(set(n1))
m1=list(set(m1))
for i in n1:
    if i in m1:
      s=s+1
print(s)
        