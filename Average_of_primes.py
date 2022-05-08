def prime(i):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    return c        
        
        
    
n=int(input())
a=list(map(int,input().split()))
s=0
k=0
for i in a:
   if prime(i)==2:
       s=s+i
       k=k+1
av="{:.2f}".format(s/k)
print(av)
   