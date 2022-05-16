n=input()
n=n.lower()
a=['a','e','i','o','u']
c=0
for i in n:
    if i in a:
        c=c+1
print(c)