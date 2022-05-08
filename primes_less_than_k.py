def prime(i):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    return c
    
n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=0
for i in a:
    if i<=k and prime(i)==2:
        s=s+1
print(s)