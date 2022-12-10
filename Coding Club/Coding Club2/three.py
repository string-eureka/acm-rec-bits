a=int(input())
for i in range (0,a):
    b=int(input())
    n = list(map(int,input("").strip().split()))[:b]
    odd = len(list(filter(lambda x: (x%2 != 0) , n)))
    even = (b-odd)
    if ((odd==even) or (odd-even==1)):
        for i in range(1, b-1, 2):
             n[i], n[i + 1] = n[i + 1], n[i]
             print(n)
    else:
         print(-1)
        