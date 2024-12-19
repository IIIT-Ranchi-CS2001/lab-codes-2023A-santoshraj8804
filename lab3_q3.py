num = int(input("Enter a number: "))

a=0
b=1
i=3
print(a)
print(b)
while(i<=num):
    c=a+b
    a=b
    b=c
    i=i+1
    print(c)