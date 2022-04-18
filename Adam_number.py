def reverse(n):
    sum=0
    while n:
        r=n%10
        n=n//10
        sum=(sum*10)+r
    return sum
n=int(input())
sq=n*n
revn=reverse(n)
sq1=revn*revn
revs1=reverse(sq1)
if sq==revs1:
    print("True")
else:
    print("False")

    


    
    
    
