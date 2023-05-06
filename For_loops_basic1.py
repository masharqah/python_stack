#basic
x=0
for x in range (0,150):
    print(x)
print ("end1")
#Multiples of five
x=0
for x in range (0,150,5):
    print(x)
print ("end2")
#Counting, the Dojo Way
y=1
for y in range (1,100):
    if (y%10 ==0 ):
        print("Coding")
    elif(y%5==0):
        print("dojo")
    else:
        print(y)

#sum of odds
sum=0
z=0
for z in range(0,500000):
    if(z%2 != 0):
        sum+= z
print("sum of numbers = " + str(sum))
#Countdown by Fours
counter=2018
while counter > 0:
    print(counter)
    counter-=4

#Flexible Counter
lowNum=0
highNum=20
mult=3
for lowNum in range (lowNum,highNum):
    if (lowNum%mult == 0):
        print(lowNum)