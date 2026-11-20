#Count no of times each word repeated in a sentence
a=input("Enter the sentence:")
low=a.lower()
split=low.split()
print(split)
word={}
for i in split:
    if i in word:
        word[i]+=1
    else:
        word[i]=1    
print("word dictionary",word)        
    
        
