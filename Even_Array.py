n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    if a[i]%2!=0:
        print("False")
        break
else:
    print("True")