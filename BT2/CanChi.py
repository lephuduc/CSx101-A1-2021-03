can = "CANH TAN NHAM QUY GIAP AT BINH DINH MAU KY ".split()
con_giap = "THAN DAU TUAT HOI TY' SUU DAN MEO TIN TY. NGO MUI".split()
n = int(input())
if n>0:
    print(can[n%10]+" "+con_giap[n%12])
else:
    n = n+1
    print(can[n%10]+" "+con_giap[n%12])