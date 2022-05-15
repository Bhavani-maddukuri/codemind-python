n=int(input())
a=list(map(int,input().split()))
so=0
se=0
for i in range(0,n):
    if i%2==0:
        se=se+a[i]
    if i%2!=0:
        so=so+a[i]
print(abs(se-so))