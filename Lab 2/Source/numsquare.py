#Taking number as input
Userinteger=int(input("Please enter a number: "))
# To avoid negative numbers as input
while Userinteger < 1:
    Userinteger = int(input("Please enter a postive number: "))
#Declare dictionary
dict={}
#Initalize dictionary key and values
for n in range(Userinteger):
    temp=n+1
    dict[temp] = temp*temp
#Print dictionary
print(dict)