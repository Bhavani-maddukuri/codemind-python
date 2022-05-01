n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    if a[i]==0 or a[i]==1:
        c=c+1
if c==n:
    print("True")
else:
    print("False")