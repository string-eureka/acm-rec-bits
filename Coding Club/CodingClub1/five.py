n, x = map(int, input().split()) #Length and Target Sum
a = list(map(int, input().split())) # List
t = {} # Hast Table method
for i in range(n): 
    if a[i] in t:
        t[a[i]] += 1
    else:
        t[a[i]] = 1 
for i in range(n):
    if (x - a[i] in t) and (x - a[i] != a[i] or t[a[i]] > 1): # Target sum reached
        print("YES")
        exit() #Exit if YES
print("NO")