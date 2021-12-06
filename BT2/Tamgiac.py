import math
def laTamGiac(a,b,c):
    if (a+b)>c and (a+c)>b and (b+c)>a:
        return True
    return False
def tamGiacVuong(a,b,c):
    if (a*a+b*b) == c*c or (a*a+c*c) == b*b or (b*b + c*c) == a*a:
        return True
    return False
def dienTich(a,b,c):
    cv=a+b+c
    p=cv/2
    dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return dt
def tamGiacDeu(a,b,c):
    return a==b and a==c
def tamGiacCan(a,b,c):
    if a==b or a==c or b==c:
        return True
    return False
a =float(input())
b = float(input())
c = float(input())
if laTamGiac(a,b,c):
    s = str(round(dienTich(a,b,c),2)).rstrip("0").rstrip(".")  
    if tamGiacVuong(a,b,c):
        print(f"Tam giac vuong, dien tich = {s}")
    elif tamGiacDeu(a,b,c):
        print(f"Tam giac deu, dien tich = {s}")
    elif tamGiacCan(a,b,c):
        print(f"Tam giac can, dien tich = {s}")
    else:
        print(f"Tam giac thuong, dien tich = {s}")
else:
    print("Khong phai tam giac")

