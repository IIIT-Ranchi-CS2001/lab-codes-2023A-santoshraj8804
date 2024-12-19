num=int(input("Enter a number: "))

i=0
sum=0
j=0
while(num>0):
    j=j+1
    i=num%10
    num=num//10
    sum+=i

print(j,sum)
