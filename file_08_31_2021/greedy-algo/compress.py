'''
Huffman's coding: is used to reduce the data size and compress it into a file
        1. here we have a text : BCCABBDDAECCBBAEDDCC  - total 20 characters
        2. if we send this text as ACSII coding then it will consume 20X8(8 bits for each ascii value) -160bits
        3. we use Huffman's coding to reduce the size of the data.
        4. please refer the pictures attached of the tables and details.
'''
import pandas as pd
messages = "BCCABBDDAECCBBAEDDCC"
print(messages)

# count_ char will count the frequency of character from the text
def count_char(text):
    new_list ={}
    for i in messages:
        if i not in new_list.keys():
            new_list[i]=messages.count(i)
    new_list ={k: v for k, v in sorted(new_list.items(), key=lambda item: item[1])}
    return new_list
# normal table created for the binary value
def create_table(n_dict):
    length = len(n_dict)
    ascii_char =[x for x in n_dict.keys()]
    ascii_count =[y for y in n_dict.values()]
    binary_value =[bin(z) for z in range(length)]
    new_table = pd.DataFrame(list(zip(ascii_char,ascii_count,binary_value)),columns =["Character"," Count","Encode Value"])
    return new_table


new_dict = count_char(messages)
new_table =create_table(new_dict)
print(new_dict)