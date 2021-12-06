def whiteBlack(n,x,y):
    y = n-y+1
    if x-y<=0:
        return "White"
    else:
        return "Black"
n = int(input())
x,y = map(int,input().split())
print(whiteBlack(n,x,y))