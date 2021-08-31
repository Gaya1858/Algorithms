

def swap_values(arr,operations):

    ind =0

    while ind < len(operations):
        index1 =operations[ind][0]
        index2 =operations[ind][1]
        if index1 != index2:
            arr[index1],arr[index2] =arr[index2],arr[index1]
            ind +=1

        else:
            arr[index1]=arr[index2]
            ind +=1
        print("index1: ",index1,"index2: ",index2,"---",arr)

    return arr

arr =[10,640,26,276,224,737,677,893,87,422,30,10,2]
opeartions =[[0,9],
             [2,2],
             [5,5],
             [1,6],
             [5,6],
             [5,9],
             [0,8],
             [6,7],
             [1,9],
             [3,3]]
print(swap_values(arr,opeartions))
