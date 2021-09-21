x = int(input())
i = int(input())
for k in range(1,100):
    f = i*k
    if f>x:
        print(k)
        break