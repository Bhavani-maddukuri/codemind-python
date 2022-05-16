n=input()
s=['a','e','i','o','u']
a=[]
for i in n:
    if i in s:
        a.append(i)
c=0
for j in s:
    if j not in a:
        print(j,end=" ")
        c=c+1

if c==0:
    print(0)
    