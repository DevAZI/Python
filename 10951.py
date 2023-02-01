while 1: 
    try:
        a, b = map(int, input().split())
        if a == None:
            break
        else:       
            print(a+b)
    except Exception:
        break

