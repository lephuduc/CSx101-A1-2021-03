online_list= []
while True:
    try:
        a,b = map(int,input().split())
        if a==1 and b not in online_list:
            online_list.append(b)
        elif a==2:
            if b in online_list:
                print(1)
            else:
                print(0)
    except:
        break
