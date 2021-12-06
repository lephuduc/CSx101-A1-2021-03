n = int(input())
k = int(input())
p = int(input())
q = int(input())

 #khoang cach toi ban tren
d1 =0
 #khoang cach toi ban duoi
d2= 0
# d = 1

# q_bob = q if k%2==0 else (3-q)
# # tru di 1 ban
# if q==1:
#   if k%2!=0:
#     d1=k//2
#     d2=(k+1)//2
#   else:
#     d1=(k-1)//2
#     d2=k//2
# else:
#   if k%2!=0:
#     d1=(k-1)//2
#     d2=k//2  
#   else:
#     d1=k//2
#     d2=(k+1)//2
  

# if p-d>0:
#     print(f"{p-d} {q_bob}")
# elif p+d==(n+1)//2 and q_bob!=2:
#     print(f"{p+d} {q_bob}")
# elif p+d<(n+1)//2:
#     print(f"{p+d} {q_bob}")
# else:
#     print(-1)
    
q_bob = q if k%2==0 else (3 - q) 

if q == 1:
  d1 = (k + 1)//2
  d2 = k // 2
else:
  d1 = k//2
  d2 = (k + 1)//2
if (p - d1)>0:
  print(p - d1,q_bob)
elif (p + d2)<=(n)//2:
  print(p + d2,q_bob)
else:
  print(-1)
