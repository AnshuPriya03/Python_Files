str1=input("Enter string1:")
str2=input("Enter string2:")
if len(str1)<len(str2):
    short=len(str1)
    long=len(str2)
else:
    short=len(str2)
    long=len(str1)
matchCnt=0
for i in range(short):
    if str1[i]==str2[i]:
        matchCnt+=1
print("Similarity between two said string:")
print(matchCnt/long)