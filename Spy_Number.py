n=int(input())
s=0
p=1
while n:
    r=n%10
    n=n//10
    s=s+r
    p=p*r
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")