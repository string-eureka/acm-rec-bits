a=int(input())
for i in range(a):
    b=int(input())
    if (b==1 or b==3):
        print("Alice")
    elif (b==2):
        print("Bob")
    elif (b%2==0):
        print("Alice")
    elif (b%2==1):
        print("Bob")