import math
t=int(input())
for _ in range(t):
    n=int(input())
    s=int(math.sqrt(n))
    if n==s*s:
        print("True")
    else:
        print("False")
    