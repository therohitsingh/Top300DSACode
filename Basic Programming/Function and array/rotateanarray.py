n = int(input())
a = []
for i in range(n):
    a.append(input())
k = int(input())
c = []
b = []
for i in range(-k,0):
    c.append(a[i])
for j in range(n-k):
    b.append(a[j])
d = c+b 
d = [str(i) for i in d]
res = int("".join(d))
print(res)


