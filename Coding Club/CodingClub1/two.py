a = int(input("")) # INPUT of range
n = list(map(int,input("").strip().split()))[:a] # INPUT LIST OF NUMBERS
print(int((((a+1)*a)/2)-sum(n))) # PRINT the difference between the sum of range and sum of list of numbers to print the missing number