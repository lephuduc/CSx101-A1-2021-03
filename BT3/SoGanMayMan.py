def laSoMayMan(n):
    for c in str(n):
        if c!="7" and c!="4":
            return False
    return True
def SoGanMayMan(n):
    count = 0
    for c in str(n):
        if c=="7" or c=="4":
            count+=1
    if laSoMayMan(count):
        return True
    return False
number = int(input())
if SoGanMayMan(number):
    print("YES")
else:
    print("NO")
