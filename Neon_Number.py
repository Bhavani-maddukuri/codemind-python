n=int(input())
s=n*n
s1=0
while s:
    r=s%10
    s=s//10
    s1=s1+r
if(s1==n):
    print("Neon Number")
else:
    print("Not Neon Number")