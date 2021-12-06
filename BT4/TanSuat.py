q  = int(input())
for i in range(q):
    n,k = map(int,input().split())
    ls = list(map(int,input().split()))
    print(ls.count(k))
