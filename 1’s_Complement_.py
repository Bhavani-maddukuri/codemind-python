n=int(input())
b=bin(n)[2:]
res=""
for i in range(len(b)):
    if b[i]=="0":
        res+="1"
    else:
        res+="0"
print(int(res,2))