n,m=map(int,input().split())
if abs(n-m)==1:
    print("Yes")
elif n==10 and m==1:
    print("Yes")
elif n==1 and m==10:
    print("Yes")
else:
    print("No")