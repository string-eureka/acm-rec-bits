a=int(input("")) #Simple Input,used because I was  unsure about using faster input templates
n=0 
n= n+ (a//5) #Divide Distance by longest possible step
a = (a%5) #Keep the remainder
n= n+ (a//4) #Did not use a loop as it would increase the time complexity , according to me
a = (a%4)
n= n+ (a//3)
a = (a%3)
n= n+ (a//2)
a = (a%2)
n= n+ (a//1)
a = (a%1)
print(n)