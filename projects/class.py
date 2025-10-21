from math import sqrt
mylist=[]
num=int(input("enter a number"))
for i in range(num):
    val=int(input("enter the value :"))
    mylist.append(val)
total=0
for elem in mylist:
    total = total+elem
    mean= total/elem
total=0
for elem in mylist:
    total=total+(elem-mean)*(elem-mean)
    variance=total/num
    stddev= sqrt(variance)

print(mean)
print(variance)
print(stddev)
