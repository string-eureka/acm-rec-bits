a=int(input(""))
for i in range (0,a):
    b,c = [int(i) for i in input("").split()] 
    n1 = list(map(int,input("").strip().split()))[:b] 
    n2 = list(map(int,input("").strip().split()))[:c] 
    n1.sort()
    n2.sort()
    if b!=c:
        print("NO")
    else:
        if  n1 == n2 :
            print("YES")
        else:
            print("NO")

