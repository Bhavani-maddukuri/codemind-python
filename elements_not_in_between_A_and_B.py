n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
d=0
for i in a:
    if i<b or i>c:
        d=1
        print(i,end=" ")
if d==0:
    print(-1)