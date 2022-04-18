n=int(input())
b=list(map(int,str(n)))
sum=0
j=1
for i in range(0,len(b)):
    h=b[i]**j
    
    sum=sum+h
    j=j+1
       
if sum==n:
    print("True")
else:
    print("False")