def pal(i):
    if i==i[::-1]:
        return True
    else:
        return False
n=input()
n=n.lower()
r=pal(n)
print(r)
    