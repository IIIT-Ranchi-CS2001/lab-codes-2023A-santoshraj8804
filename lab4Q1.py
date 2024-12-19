sent="my name is simar madam"
s=sent.split()

count=0
for i in range(len(s)):
    if(s[i]==s[i][::-1]):
        count+=1

print("The number of palindromes are: ",count)