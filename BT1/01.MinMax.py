a,b = map(int,input().split())
max = a
min = b
if a<b:
    max = b
    min = a
print("max = "+ str(max))
print("min = "+str(min))
