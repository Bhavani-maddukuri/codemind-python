a,b=map(int,input().split())
a1=[]
b1=[]
j=0
c1=[]
for i in range(1,a+b):
   c=a*i
   d=b*i
   a1.append(c)
   b1.append(d)
for i in range(0,len(a1)):
   if a1[i] in b1:
      print(a1[i])
      break