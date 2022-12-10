t = int(input())
for i in range(t):
    n, k = map(int, input().split())

    b = list(map(int, input().split()))
    a1 = b[0] - (b[1] - b[0])

    is_possible = True
    if a1 < 0:
        is_possible = False
    else:
        for i in range(1, n):
            ai = b[i] - sum(b[:i])
            if ai < 0 or (i > 1 and b[i - 1] > b[i]):
                is_possible = False
                break
    if is_possible:
        print("YES")
    else:
        print("NO")
