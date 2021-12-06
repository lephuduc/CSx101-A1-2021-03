def fibonacci(n):
    s1 = 0
    s2=1
    for i in range(n):
        tmp = s1
        s1 = s2
        s2 = tmp+s2
    return s1
n = int(input())
if n>0:
    print(fibonacci(n))
else:
    print(-1)