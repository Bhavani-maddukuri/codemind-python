n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=0
for i in range(0,n):
    if i>=k:
        break
    else:
        s=s+a[i]
        #print(a[i])
print(s)
    