t = int(input())
for i in range(t):
    x = int(input())
    b = [int(bit) for bit in bin(x)[2:]]
    b = [1 - bit for bit in b]
    y = int(''.join(str(bit) for bit in b), 2)
    print(y)