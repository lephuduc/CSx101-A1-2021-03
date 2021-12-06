import math
n,x = map(int,input().split())
#bien dem
count = 0
for i in range(1,int(math.sqrt(x))+1):
    if (x%i==0) and (i<=n) and (x//i<=n):
        if i == x//i:
            count += 1
        else:
            count+=2
print(count)
    
