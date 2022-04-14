def proni(n):
    p=1
    a=0
    b=1
    while p<=n:
        
        p=a*b
        if p==n:
            return "YES"
            
        else:
            a=a+1
            b=b+1
    else:
        return "NO"
    
    
        
    

n=int(input())
s=proni(n)
print(s)
