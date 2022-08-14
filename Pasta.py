n,m=map(int,input().split())
a1=list(map(int,input().split()))
b1=list(map(int,input().split()))
c=0
for i in range(m):
    if b1[i] in a1:
        a1.remove(b1[i])
        c+=1
    else:
        print("No")
        break
if c==m:
    print("Yes")
    
    