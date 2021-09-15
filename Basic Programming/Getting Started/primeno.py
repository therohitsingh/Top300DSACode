x = int(input())
a = []

for i in range(x):
    a.append(int(input()))

for i in range(x):
    m = a[i]//2
    for j in range(2,m+1):
        if(a[i]%j==0):
            print("not prime")
            break
    else:
        print("prime")    




