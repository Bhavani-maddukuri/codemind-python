n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
   d=0
   for j in range(0,i):
       if a[i]==a[j]:
         d=1
         break
   if d==0:
     print(a[i],end=" ")