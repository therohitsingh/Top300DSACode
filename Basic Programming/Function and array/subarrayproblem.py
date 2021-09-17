#print all the subarray in an array 
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

for i in range(0,n):
    for j in range(i,n):
        for k in range(i,j+1):
            print(a[k],end="  ")
        print("\n")    