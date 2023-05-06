#Biggie Size 
def bigge(a):
    for i in range (0,len(a)):
        if (a[i]>0):
            a[i]="Big"
    return a 
#count positives 
def count_positives(a):
    count=0
    for i in range (0,len(a)):
        if (a[i]>0):
            count += 1
    a[len(a)-1]=count
    return a
# Sum Total 
def sum_total(a):
    sum=0
    for i in range (0,len(a)):
        sum += a[i]
    return sum 

x = sum_total([5,6,7,2])

#Average 
def avg (a):
    m = sum_total (a)/len(a)
    return m
print (avg([5,6,7,2]))
# length 
def length(a):
    if len(a)<2:
        return False
    return len(a)
#Minimun
def minimum(a):
    min=a[0]
    for i in range (1, len(a)):
        if a[i]<min:
            min = a[i]
    return min
        

print (minimum ([7,3,2,3,6,-7,2,0]))


#Maximum
def maxi(a):
    max=a[0]
    for i in range (1, len(a)):
        if a[i]>max:
            max = a[i]
    return max
        

print (maxi ([7,3,2,3,6,-7,2,100]))

#ultimate analysis 
def ultimate_analysis (a):
    x= {'sum-total':sum_total(a), 'average': avg(a), 'Minimum': min (a), 'Maximum': maxi(a), 'length':length(a)}
    return x

print (ultimate_analysis([5,10,15,10,15]))

#reverse list 
def rev(a):
    for i in range (len(a)//2):
        a[i]=a[len(a)-i-1]
        a[len(a)-i-1] = a[i]
    return a

print (rev([5,7,3,4,6,9,0]))


