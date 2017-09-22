#User input!
t=input("Enter the words separated by commas: ")
#splitting words separated by commas which are automatically stored as a list.
w=t.split(",")
#sorting the list.
w1=sorted(w)
#iterating through sorted list and printing output.
for k in w1[:-1]:
    print(k+",",end='')
print(w1[-1])
