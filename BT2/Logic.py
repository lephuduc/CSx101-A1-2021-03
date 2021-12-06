def logic(ls):
    if ls[0]=="1":
        if ls[1]=="0":
            return False
    if ls[1]=="1":
        if ls[2]=="0":
            return False
    if ls[1]=="0" and ls[2]=="1":
        if ls[3]=="0":
            return False
    return True

ls = input().split()
if logic(ls):
    print(1)
else:
    print(0)