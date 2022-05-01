n=int(input())
a=list(map(int,input().split()))
s1=sum(a)//n
#print(s1)
c=0
for i in range(0,n):
    if a[i]<=s1:
        c=c+1
        
print(c)
       
