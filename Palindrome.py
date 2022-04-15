def pal(n):
    s=0
    temp=n
    while n:
        r=n%10
        n=n//10
        s=(s*10)+r
    if s==temp:
        return True
    else:
        return False
n=int(input())
pal(n)
if pal(n):
    print("True")
else:
    print("False")
