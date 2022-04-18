n=int(input())
sum=0
while n:
    r=n%10
    n=n//10
    sum=sum*10+r
print(sum)    
    