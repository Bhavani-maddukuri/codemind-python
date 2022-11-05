def per(r):
    p=1
    for i in range(2,r+1):
        p=p*i
    return p
n=int(input())
s=0
t=n
while n!=0:
    r=n%10
    n=n//10
    s=s+per(r)
if s==t:
    print("The number",t,"is a strong number")
else:
    print("The number",t,"is not a strong number")
    
    