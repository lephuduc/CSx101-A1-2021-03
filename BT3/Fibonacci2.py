def fibonacci(n):
    if n==1 or n==2:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)

x = int(input())
if x >=1 and x <= 30:
    print( fibonacci(x))
else:
    print(f"So {x} khong nam trong khoang [1,30].")