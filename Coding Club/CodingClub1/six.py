n,a,b = [int(i) for i in input("").split()] # INPUT length and price
d=input("")#Input Order history
mb = (2*b)*d.count('BB')# Count 2 B dish orders and price
d=d.replace('BB','')# Remove them from the string
mb += (a+b)*d.count('BA')#Do the same with BA
d=d.replace('BA','')
ma=a*(d.count('A'))# Count Alice's orders and price
print(ma,mb)
