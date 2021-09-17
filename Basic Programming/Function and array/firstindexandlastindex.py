def firstandlastindex(a,n,k):
    for i in range(0,n):
        if a[i]==k:
            print(i)
    for j in range(n-1,-1,-1):
        if a[j]==k:
            print(j)


n = int(input())
a = []
for i in range(n):
    a.append(input())   
k = int(input())
firstandlastindex(a,n,k)