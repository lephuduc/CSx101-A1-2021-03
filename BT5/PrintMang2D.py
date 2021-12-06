ls = []
ls_max = []
r,c = map(int,input().split())
for i in range(r):
    element = input().split()
    max_len = element[0]
    for s in element:
        if len(s) > max_len:
            max_len = len(s)
    ls_max.append(max_len)
    ls.append(element)
