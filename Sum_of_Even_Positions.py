n=int(input())
a=list(map(int,input().split()))
so=0
for i in range(0,n):
    if i%2==0:
        so=so+a[i]
print(so)