#Counting the word frequency in a file

file1 = open('paragraph','r')
paragraph_file = file1.read().lower()
occurence = {}
for word in paragraph_file.split(" "):
    if not word in occurence:
      occurence[word] = 1
    else:
     occurence[word] = occurence[word]+1
print(len(occurence))
for key,number in occurence.items():
           print ('"',key,'"',':',number)