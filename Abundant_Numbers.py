def sf(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return sum       
n=int(input())
sf1=sf(n)

if sf1>n:
    print("True")
else:
    print("False")
