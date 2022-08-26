num=int(input("Enter a number:"))
a=0
b=1
sum=0
if num<=0:
    print(" Enter number greater than 0:")
else:
    for i in range(0,num):
        print(sum,end=" ")
        a=b
        b=sum
        sum=a+b
        
