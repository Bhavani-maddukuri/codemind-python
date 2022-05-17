n=input()
n=n.split()
v="aeiouAEIOU"
for i in n:
    c=0
    a=list(i)
    for j in a:
        if j in v:
            c=c+1
    print(c,end=" ")    