#countdown

def countdown(x):
    list=[]
    for x in range (x,-1,-1):
        list.append(x)
    return list

output = countdown(7)
print(output)

# Print and Return 
def print_and_return(a,b):
    print(a)
    return b

#First Plus Length 
def first_plus_length (a):
    value= a[0]+ len(a)
    return value

print (first_plus_length([1,4,3,2,1,4,6,8,4,0,44]))

#Values Greater than Second

def values_greater_than_second (b):
    x=[]
    if (len(b)<=1):
        return False
    else:
        for i in range(0, len(b)):
            if (b[i] > b[1]):
                x.append(b[i])
        print (x)
        return x

values_greater_than_second ([5,2,3,2,1,4])

#Length and value 
def length_and_value(c,d):
    x=[]
    for i in range (0,c):
        x.append(d)
    print(x)
    return x
length_and_value(5,8)




