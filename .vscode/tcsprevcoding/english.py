n = input()
n = n.split(" ")
count = 0
maxi = 0
for i in range(len(n)):
    count = len(n[i])
    maxi = max(count,maxi)
print(maxi)    