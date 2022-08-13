t=int(input())
for _ in range(t):
    d=int(input(),16)
    b=bin(d)[2:]
    b=str(b)
    c=((((len(b)//4)+1)*4))
    
    if (len(b))%4!=0:
        print(b.zfill(c))
        
    else:
        print(b)