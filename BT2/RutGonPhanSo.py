import math

n = int(input())
for i in range(n):
    tu,mau = map(int,input().split())
    ucln = math.gcd(tu,mau)
    tu = tu//ucln
    mau= mau//ucln
    if mau!=1:
        print(f"{tu} {mau}")
    else:
        print(tu)