# find the ceil and floor value of a no. in a sorted array 
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
l = 0
h = n-1
ceil = 0
floor = 0
while(l<=h):
    mid = (l+h)//2
    if a[mid]<d:
        l = mid+1
        ceil=a[mid]
    elif a[mid]>d:
        h = mid-1
        floor=a[mid]
    else:
        ceil=floor=a[mid]
print(floor)
print(ceil)                