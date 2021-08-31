
def reverse1(s):
    return "*".join(s.split()[::-1])
    # return "".join(reversed(s.split()))
    # s = s.split()
    # print(s)
    # s.reverse()
    # print(s)
# first split the string

def rev(s):

    length =len(s)
    i =0
    spaces =[' ']
    words =[]
    while i < length:
        if s[i] not in spaces:
            word_start =i
            while (i<length) and (s[i]  not in spaces):
                i +=1
            words.append(s[word_start:i])
        i+=1
    print(''.join(reversed(s)))



x ="This is the best"
rev(x)
# print((''.join(reversed(x))))

y=["This is the best"]

# for string
seq_string = 'Python'
print("".join(list(reversed(seq_string))))

# for tuple
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seq_tuple)))

# for range
seq_range = range(5, 9)
print(list(reversed(seq_range)))

# for list
seq_list = [1, 2, 4, 3, 5]
print(list(reversed(seq_list)))