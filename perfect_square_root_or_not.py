n=int(input())
for i in range(1,n//2):
    if (n/i==i):
        print("True")
        break
else:
    print("False")
