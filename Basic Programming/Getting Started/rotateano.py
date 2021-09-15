n = input()
k = int(input())
a = ""
b = ""
a+=n[-k:]
m = len(n)
m = m-k
for i in range(m):
    b+=n[i]
print(a+b)    