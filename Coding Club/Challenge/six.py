a=int(input())
for i in range (a):
    n,m = [int(i) for i in input().split()] 
    x = list(map(int,input().strip().split()))[:n] 
    newx=[pow(5,j) for j in x]
    newx.sort()
