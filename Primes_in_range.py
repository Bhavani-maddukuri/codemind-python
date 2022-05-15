import math
def prime(j):
    c=0
    if j==1:
        c=1
    for i in range(2,int(math.sqrt(j))+1):
        if j%i==0:
            c=c+1
            break
    
    if c==0:
        return True
    if c==1:
        return False
m=int(input())
n=int(input())
s=0
for j in range(m,n+1):
    if prime(j):
        s=s+1
print(s)
