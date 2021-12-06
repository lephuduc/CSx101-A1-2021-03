ls = []
x = 0
y = 0
for i in range(5):
    j = input().split()
    if "1" in j:
        x = i
        y = j.index("1")
    ls.append(j)
# print(f"{x} {y}")
step = 0
if x==0 or x ==4:
    step += 2
if x == 1 or x ==3:
    step += 1
if y==0 or y ==4:
    step += 2
if y == 1 or y ==3:
    step += 1
if x ==2 and  y==2:
    step = 0
print(step)
