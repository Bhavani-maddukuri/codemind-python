for _ in range(int(input())):
    n=int(input())
    b=1
    for i in range(2,n+1):
        if i%2==0:
            b^=i
        else:
            b&=i
    print(b)