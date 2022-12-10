a=int(input())
for i in range (a):
    n,x = [int(i) for i in input().split()] 
    ray = list(map(int,input().strip().split()))[:n] 
    s1 = 0
    s2 = 0
    for i in range(x):
        s2 += ray[i]
    s1 = s2
    for i in range(x, n):
        s2 = s2 - ray[i - x] + ray[i]
        s1 = max(s1, s2)
    print(s1)
