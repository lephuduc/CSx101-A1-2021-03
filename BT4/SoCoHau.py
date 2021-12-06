
end,m = input().split()

count=0


if len(end)< len(m):
    temp = m[-len(end):]
    if int(temp) >= int(end):
        count=1
    count=count+int(m[:-len(end)])
elif len(end) == len(m) and end<m:
    count = 1
print(count)

