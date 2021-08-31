'''
Array pair sum

'''

def pair_sum(array, k):
    if len(array) <2:
        return print("too small")
    seen = set()
    output =set()
    for num in array:
        target = k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))
    print('\n'.join(map(str,list(output))))
    print(output)

def find_sum_of_two(A, val):
    found_values = set()
    for a in A:
        if val - a in found_values:

            return True

        found_values.add(a)
    print(found_values)
    return False
pair_sum([1,3,2,2,5,9],8)
print(find_sum_of_two([1,3,2,2,9],8))