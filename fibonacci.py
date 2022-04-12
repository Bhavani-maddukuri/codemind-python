n=int(input())
a=0
b=1
print(a,b,end=" ")
sum=0
for i in range(2,n):
    sum=a+b
    a=b
    b=sum
    print(sum,end=" ")