import math
n = 10**15-1
sum = 1

for i in range(2,int(math.sqrt(n))):
    if n%i == 0:
        if i == n//i:
            sum += i
        else:
            sum += i +n//i
print(sum)