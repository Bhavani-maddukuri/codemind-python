n=int(input())
a=list(map(int,input().split()))
s=sum(a)
k=s//n
for i in a:
    if k==i:
        print("True")
        break
else:
    print("False")