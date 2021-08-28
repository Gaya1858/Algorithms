import functools


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
#print(b*(bool)(b // a))

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

#print(multiply(-20,-10))

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
    remainder =0
    while (dividend >= divisor):
        dividend -= divisor
        quotient += 1
        remainder=dividend

    #if the sign value computed earlier is -1 then negate the value of quotient

    if sign ==-1:
        quotient=-quotient

    return f"the quotient is: {quotient}, and the remainder is: {remainder}"


# Driver code
a = 10
b = 3
#print(divide(a, b))
a = 43
b = -8
#print(divide(a, b))
def adds(x,y):

    while (y != 0):
        # carry now contains common
        # set bits of x and y
        carry = x & y
        # Sum of bits of x and y where at
        # least one of the bits is not set
        x = x ^ y

        # Carry is shifted by one so that
        # adding it to x gives the required sum
        y = carry << 1
    return x

#print(adds(12,8))

#/*******************************************/#
# sorted merge
def sorted_merge(a,b):
    x =0
    y =0
    new_array =[]
    while x<len(a) and y<len(b):
        if(a[x] <b[y]):
            new_array.append(a[x])
            x+=1
        else:
            new_array.append(b[y])
            y+=1
    if(x < y):
        new_array.append(a[x])
    elif y< x:
        new_array.append(b[y])

    return new_array

#print(sorted_merge([1,13,14,25,77,99],[5,7,9,24,27,98]))
# sorted merge and adding elements to one of the array
def sorted_merge1(a,b):
    x =0
    y =0
    while x<len(a) and y<len(b):
        if(a[x] <b[y]):
            x+=1
        else:
            a.insert(x,b[y])
            y+=1
            x+=1
    return a

#print(sorted_merge1([1,13,14,25,77,99],[5,7,9,24,27,98]))

#/*******************************************/#

@functools.lru_cache(maxsize=None)
def fib1(n):
    if(n ==0 or n ==1):
        return n
    else:
        return fib1(n-1)+fib1(n-2)

### Memorization of recursive funtion
fibcache = {}
def fib(num):
    if num in fibcache:
        return fibcache[num]
    else:
        fibcache[num] = num if num < 2 else fib(num-1) + fib(num-2)
        return fibcache[num]
#print(fib(7))

### Memorization of recursive funtion
factorial_memo = {}
def factorial(k):
    if k < 2: return 1
    if k not in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
    return factorial_memo[k]

print(factorial(7))