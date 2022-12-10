a=int(input(""))
n = list(map(int,input("").strip().split()))[:a] 
t=0
for i in range(a - 2):
  if n[i] + n[i + 1] == n[i + 2]:
    t += 1
  elif abs(n[i] - n[i + 1]) == n[i + 2]:
    t += 1
print(t)
