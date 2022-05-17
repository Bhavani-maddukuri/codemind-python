def pal(i):
    if i==i[::-1]:
        return True
    else:
        return False
n=input()
n=n.lower()
n=n.split()
c=0
for i in n:
    if pal(i):
        c=c+1
print(c)
    