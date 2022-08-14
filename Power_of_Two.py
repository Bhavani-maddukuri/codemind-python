n=int(input())
r=0
i=0
while n>r:
    r=1<<i
    if r==n:
        print("True")
        break
    i=i+1
else:
    print("False")
    