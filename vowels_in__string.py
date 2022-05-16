n=input()

n=list(n)
a=['a','e','i','o','u','A','E','I','O','U']
s=[]
r=[]
for i in n:
    if i in a:
        s.append(i)
for i in s:
    if i not in r:
        r.append(i)
print(' '.join(r))