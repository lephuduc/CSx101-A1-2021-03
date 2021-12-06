a,b,c=list(map(float,input().split()))
result = pow(a,5) - 2*(pow(abs(b),0.5)) + a*b*c
print("%.2f"%result)