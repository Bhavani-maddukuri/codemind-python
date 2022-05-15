n=int(input())
a=list(map(int,input().split()))
so=0
for i in a:
    if i%2!=0:
        so=so+i
print(so)