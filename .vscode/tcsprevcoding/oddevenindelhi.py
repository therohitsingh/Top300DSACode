n = int(input())
a = []
b= []
for i in range(n):
    a.append(int(input()))
if n%2!=0:
    print(a)
else:
    l = 0
    h = n
    mid = l+h//2
    for i in range(0,n):
        if a[i]==a[mid]:
            k = a[mid]+a[mid-1]
            del a[mid-1]
            b.append(k)
            
        else:
            b.append(a[i])
print(b)
       
