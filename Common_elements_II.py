n,m=map(int,input().split())
n1=list(map(int,input().split()))
m1=list(map(int,input().split()))
a=[]
#n1=list(set(n1))
#m1=list(set(m1))
for i in n1:
    
    if i not in m1:
        print(i,end=" ")
for j in m1:
    if j not in n1:
        print(j,end=" ")
