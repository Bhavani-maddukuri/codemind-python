def auto(n):
    s=n*n
    while n:
        if(n%10!=s%10):
            return False
        n=n//10
        s=s//10
    return True
n=int(input())
if auto(n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    
