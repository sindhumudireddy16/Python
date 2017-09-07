lowvalue = int(input('enter the lowest value:'))
highvalue = int(input('enter the highest value'))

for i in range(lowvalue,highvalue + 1):
 if(i%5==0 and i%2==0):
     print(i,end=',')