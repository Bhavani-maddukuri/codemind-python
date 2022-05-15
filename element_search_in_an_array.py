n=int(input())
a=list(map(int,input().split()))
k=int(input())
for i in a:
    if k==i:
        print("True")
        break
else:
    print("False")