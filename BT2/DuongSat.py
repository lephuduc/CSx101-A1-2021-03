
k,t = list(map(int,input().split()))
# truong hop chan
if t%k ==0:
    n = t//k
    if n%2==0:
        print(t%k)
    else:
        print(k - t%k)
else:
    n = t//k
    if n%2!=0:
        print(k - t%k)
    else:
        print(t%k)
