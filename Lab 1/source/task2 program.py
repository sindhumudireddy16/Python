stringalpha = 'abcdefghijklmnopqrstuvwxyz'
set1 = set(stringalpha)
string1 = input('Enter a string:')
str = string1.lower()
set2 = set(str)
if set2==set1:
    print("The entered string  contains all alphabets")
else:
  print("The entered string donot contains all the alphabets")