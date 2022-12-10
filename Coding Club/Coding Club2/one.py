a=int(input())
n = list(map(int,input("").strip().split()))[:a]
count_2 = 0
count_5 = 0
for x in n:
    while x % 4 == 0:
        x //= 4
        count_2 += 1
    while x % 5 == 0:
        x //= 5
        count_5 += 1
print(min(count_2, count_5))
