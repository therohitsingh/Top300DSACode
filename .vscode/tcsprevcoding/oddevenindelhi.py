n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
D = int(input())
F = int(input())
count = 0
if D%2 ==0:
    for i in range(n):
        if a[i]%2!=0:
            count+=1
    print(F*count)        
else:
    for j in range(n):
        if a[j]%2==0:
            count+=1
    print(F*count)        

        
