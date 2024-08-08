sentence=input("Enter a sentence:")
wordList=sentence.split(" ")
print("The sentence has",len(wordList), "words")
digCnt=upCnt=loCnt=0
for ch in sentence:
    if '0'<=ch<='9':
        digCnt+=1
    elif 'A'<=ch<='Z':
         upCnt+=1
    elif 'a'<=ch<='z':
        loCnt+=1
print("The santence has",digCnt,"digits",upCnt, "uppercase and",loCnt, "lowercase")