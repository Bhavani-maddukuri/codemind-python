n=int(input())
if n==0 or n==1:
    print(True)
a=0
b=1
sum=a+b
while sum<n or sum==n:
    sum=a+b
    a=b
    b=sum
    
    if n==sum:
        print("True")
        break
else:
    print("False")
    

    
    
