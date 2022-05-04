def fun():
    s=0
    v=[]
    for i in a:
        if i not in v:
            v.append(i)
    for i in range(0,len(v)):
        if v[i]==a.count(v[i]):
            s=1
            print(v[i],end=" ")
    if s==0:
        print(-1)
n=int(input())
a=list(map(int,input().split()))
fun()