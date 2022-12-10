a = int(input("")) # TestCases
for i in range (0,a):
    b = int(input(""))# Length of LIST
    n = list(map(int,input("").strip().split()))[:b] # LIST
    print('YES' if len(list(set(n)))==1  else 'NO') #Prints yes if all elements are the same, else no
    