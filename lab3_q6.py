str = input("Enter string: ")
check = input("Enter the char. to check: ")

a=0
for i in range(len(str)):
    if(str[i]==check):
        a=a+1

print(a)