import re
docName = "brown-train.txt"
text = ''.join(open(docName).readlines())
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
list = []
for s in sentences :
    list.append('<s>'+" " + s + " " + '</s>' + " ")
#print(list)
article = [s.lower() for s in list]
#print(list2)

dict = {}

originalTotalWord = 0
for s in article :
    for c in s.split() :
        originalTotalWord += 1
        if c in dict :
            dict[c] += 1
        else :
            dict[c] = 1
#print(dict)
#print(totalNumWords)

#print(article)

newArticle = []
for s in article :
    for c in s.split() :
        if c in dict and dict[c] == 1 :
            #print(s)
            newArticle.append(c.replace(c,"<unk>"))
            #print(s.replace(c,"<unk>"))
        else :
            newArticle.append(c)

#print(newArticle)
#after cleaned everything and replaced with <unk>
newDict = {}
totalTokens = 0
for s in newArticle :
    for c in s.split() :
        totalTokens += 1
        if c in newDict :
            newDict[c] += 1
        else :
            newDict[c] = 1
#print(dict)
#Q1:
print("answer for Q1 : ")
print(len(newDict))
#Q2 : (inclduing padding & unk)
print("answer for Q2 : ")
print(totalTokens)
