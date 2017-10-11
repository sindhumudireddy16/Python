#import modules
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

#reading text file
sample_text=open("sample.txt")
s=sample_text.read()

#deleting all words which are other than nouns
uselesswords = set(stopwords.words('english'))
token_words = word_tokenize(s)
remainingwords = [word for word in token_words if not word in uselesswords]
for word in token_words:
    if word not in uselesswords:
        remainingwords.append(word)
print("Tokenization")

print(token_words)
print("After deleting useless words or prepositions")
print ("--------------------------------")
print(remainingwords)

#applying lemmatization
list1=[]
for i in remainingwords:
    lemmatizer = WordNetLemmatizer()
    l=lemmatizer.lemmatize(i,pos='v')
    list1.append(l)
print("lemmatization:")

print(list1)


#applying POS, removing the verbs
z=pos_tag(remainingwords)
print("POS tagging:")

print(z)
list2=[]
list3=[]
for (x,y) in z:
    if (y != 'VB') and (y != 'VBD') and (y != 'VBG') and (y != 'VBN') and (y != 'VBP') and (y != 'VBZ') and (x != ',') and (x != '.'):
        list2.append(x)
print("After removal of verbs:")

print(list2)

#Calculate the word frequency of the remaining words
import collections
temp=collections.Counter(list2)
print("frequency of word: ")

print(temp)

#Summary consisting of sentences with most repeated words.
print("Summarization:")

for sentence in open("sample.txt"):
    if (("home" in sentence) or ("animal" in sentence) or ("cat" in sentence) or ("I" in sentence) or ("she" in sentence)):
        print(sentence)