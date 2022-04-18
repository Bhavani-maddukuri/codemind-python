def pal(n):
    sum=0
    
    while n:
        r=n%10
        n=n//10
        sum=sum*10+r
    return sum
       
n=int(input())
t=n
temp=n
while True:
    n=n+1
    x=pal(n)
    
    if x==n:
        
        break
    
while True:
    t=t-1
    y=pal(t)
    if y==t:
        break
    
if abs(x-temp)<abs(y-temp):
    print(x)
if abs(x-temp)==abs(y-temp):
    print(y,x)
if abs(x-temp)>abs(y-temp):
    print(y)
        