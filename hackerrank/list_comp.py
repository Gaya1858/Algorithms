
def list_co (x,y,z,n):
    new_list =[[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c !=n]
    return new_list


x =1
y=1
z=1
n=2
#print(list_co(x,y,z,n))

n =5
arr =[57, 57,-57,57]
new_l =sorted(list(set(arr)))[-2]


#print(new_l)
import re

def minion_game(string):
    # your code goes here
    stuart =0
    kevin =0
    vowels ="AEIOU"
    for i in range(len(string)):
        if string[i] not in vowels:
            stuart += (len(string)-i)
        else:
            kevin+= (len(string)-i)

    if(kevin>stuart):
        print("Kevin ",kevin)
    elif(kevin == stuart):
        print("Draw")
    else:
        print("Stuart ",stuart)

#minion_game("BANANANAAAS")

def split_and_join(line):

    # write your code here
    new_list = line.split()
    new_string ="-".join(new_list)
    print(new_string)
#split_and_join("this is a string ")

def merge_the_tools(string, k):

    set1 ={}
    count =0
    length =0
    while count<len(string):
        if(string[count] not in set1):
            set1[string[count]] =1
        length+=1
        if(length ==k):
            print("".join(set1.keys()))
            length=0
            set1.clear()
        count+=1





merge_the_tools('AABCAAADA',3)
