t=int(input())
for _ in range(t):
    n=int(input())
    b=bin(n)[2:]
    print(b.count("1"))