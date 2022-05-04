def fun(n):
   sum=0
   while n:
      r=n%10
      sum=sum*10+r
      n=n//10
   return sum
n=int(input())
if n>=0:
   print(fun(n))
elif n<0:
   print(-fun(-n))