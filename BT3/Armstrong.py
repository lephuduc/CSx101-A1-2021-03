def isArmstrong(n):
    m = len(str(n))
    sum = 0
    for i in str(n):
        sum+=(int(i))**m
    return sum == n

n = int(input())
print(isArmstrong(n))
