n=int(input())
a=list(map(int,input().split()))
f=0
l=0
for i in a:
       if i<=n//2:
        f=f+i
       else:
           l=l+i
print(abs(f-l))
    