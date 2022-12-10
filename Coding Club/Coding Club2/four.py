x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
a=(((x1)*(y3-y2))+((x2)*(y1-y3))+((x3)*(y2-y1)))/((x1-x2)*(x2-x3)*(x1-x3))

b=(y2-y1/(x2-x1))-((x1+x2)*a)

c=((-a)*(pow(x3,2)))+ ((-b)*(x3))+y3

print(a+b+c)