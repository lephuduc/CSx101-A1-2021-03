def BanHang(n,ls):
    gia_goc= sum(ls)
    avg = gia_goc/n
    i = int(avg)
    if gia_goc%n == 0:
        return i
    else:
        return i+1
q = int(input())
for i in range(q):
    n = int(input())
    ls = list(map(int,input().split()))
    print(BanHang(n,ls))