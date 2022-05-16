n=input()
n=list(n)
k=input()

a=['a','e','i','o','u']

for i in range(0,len(n)):
    
    if n[i]==k:
        print("True")
        print(i)
        break
else:
    print("False")
