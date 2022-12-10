n=int(input())
arr=[*range(1,n+1)]
print(arr)
for i in range (n):
    
    hash = [0]*(n + 1)
    x=0
    # Counting the frequency
    for i in range(n) :
        hash[arr[i]] += 1
 
    # Check if each frequency is 1 only
    for i in range(1, n + 1):
        if (hash[i]==0):
            x=x+1
       
    
 
