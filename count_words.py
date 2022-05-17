n=input()
n=n.split()
v="aeiouAEIOU"
c=0
for i in n:
    a=list(i)
    
    if a[0]  in v:
        if a[len(a)-1] not in v:
            
            c=c+1
print(c)         