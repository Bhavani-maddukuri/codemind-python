import math
def prime(j):
    c=0
    if j==1:
        c=1
    for i in range(2,int(math.sqrt(j))+1):
        if j%i==0:
            c=c+1
            break
    
    return c
n=int(input())
s=0
for j in range(1,n+1):
    if n%j==0:
        if prime(j)==1:
            s=s+1
print(s)
