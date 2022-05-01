n=int(input())
a=list(map(int,input().split()))
s=0
j=-1
for i in range(n-1,-1,-1):
    j=j+1
    s=s+(a[i]*(2**j))
    
print(s)    