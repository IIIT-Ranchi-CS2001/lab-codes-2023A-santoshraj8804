str = input("Enter string: ")

s=False
for i in range(len(str)):
    if(str[i]>='A' and str[i]<='Z'):
        s=True
    elif(str[i]>='a' and str[i]<='z'):
        s=True
    elif(str[i]>='0' and str[i]<='9'):
        s=True
    else:
        s=False
        break

print(s)