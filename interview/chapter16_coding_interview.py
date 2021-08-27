
def swap(a,b):
    a = a-b
    b = b+a
    a = b-a

    return a,b

#print(swap(15,30))


def swap_bin(a,b):
    a = a^b # XOR will return true if one of the value is true int he given bin and return false if both the values
    # are true or false
    # a =101 and b =110, will check 2^0 th position and one of the value is 1 which true
    # 2^1 position a has 0 and b has 1 so returns 1
    b = b^a
    a = b^a

    return a,b

#print(swap(1001,1100))

#/*******************************************/#

# Word frequencies
def word_freq(array,word):
    word_counter = {}
    word =word.lower()
    for i in array:
        if i.lower() == word:
            if word in word_counter:
                word_counter[word] +=1

            else:
                word_counter[word]=1
    return word_counter


words =[ "menaka",'muyal','juoal','muyal','muyal','hether',"menaka",'muyal','juoal','muyal','muyal','hether']
#print(word_freq(words,'muyal'))
def word_freq1(array):
    word_counter ={}
    for i in array:
        if i in word_counter:
            word_counter[i] +=1
        else:
            word_counter[i] =1
    return word_counter


words =[ "menaka",'muyal','juoal','muyal','muyal','hether',"menaka",'muyal','juoal','muyal','muyal','hether']
#print(word_freq1(words))

#/*******************************************/#
# given two arrays of integers of integers, computer the pair of values with smallest non negative
# difference. return the difference

def small_difference(a,b):
    small_diff = abs(a[0] - b[0])
    values =set()
    for i in a:
        for j in b:
            diff =abs(i-j)
            if(diff< small_diff):
                small_diff =diff
                values =(i,j)

    return f" difference is: {small_diff} and the pair is: {values}"

#print(small_difference([1,3,15,11,2],[23,127,235,19,8]))

# optimal approach with sorted array
def small_difference1(a,b):
    aCount=0
    bCount=0
    values =set()
    small_diff= abs(a[0]-b[0])
    while aCount<len(a) and bCount< len(b):
        diff =abs(a[aCount]-b[bCount])
        if(diff < small_diff):
            small_diff=diff
            values =(aCount,bCount)
        if(a[aCount]<b[bCount]):
            aCount+=1
        else:
            bCount+=1

    return f" difference is: {small_diff} and the pair is: {values}"

#print(small_difference1([1,2,3,11,12,15],[7,9,19,23,127,235]))
#/*******************************************/#
# number max: find maximum of two numbers with out using conditions or comparison operators
# Function to find the largest number
def largestNum(a, b):
    return (a * (bool)(a // b)) + (b * (bool)(b // a))

# Driver Code
a = 22
b = 1231
print(b*(bool)(b // a))

#/*******************************************/#
#  operations : multiply, divide and subtract using add operator only

def multiply(a,b):
    sum =0
    if(a >0 and b>0):
        for i in range(1,a+1):
            sum +=b
        return sum
    elif b>0 and a<0:
        for i in range(1,(b+1)):
            sum += a
        return sum
    elif b<0 and a>0:
        for i in range(1,(a+1)):
            sum += b
        return sum
    else:

        for i in range(-1,(a)-1,-1):
            sum += (-b)
        return sum

print(multiply(-20,-10))

# divide
# Function to divide a by b and
# return floor value it
def divide(dividend, divisor):

    # Calculate sign of divisor i.e.,
    # sign will be negative only iff
    # either one of them is negative
    # otherwise it will be positive
    sign = -1 if ((dividend < 0) ^  (divisor < 0)) else 1
    # Update both divisor and
    # dividend positive
    dividend = abs(dividend)
    divisor = abs(divisor)

    # Initialize the quotient
    quotient = 0
    while (dividend >= divisor):
        dividend -= divisor
        quotient += 1

    #if the sign value computed earlier is -1 then negate the value of quotient

    if sign ==-1:
        quotient=-quotient

    return quotient


# Driver code
a = 10
b = 3
print(divide(a, b))
a = 43
b = -8
print(divide(a, b))

