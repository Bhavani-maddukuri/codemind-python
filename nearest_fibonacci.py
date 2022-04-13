n=int(input())
a=0
b=1
s=0
while True:
     s=a+b
     a=b
     b=s
     if s<=n:
         x=s
     if s>n:
         y=s
         break
if abs(x-n)<abs(y-n):
    print(x)
if abs(x-n)==abs(y-n):
    print(x,y)
if abs(x-n)>abs(y-n):
    print(y)
     


          
