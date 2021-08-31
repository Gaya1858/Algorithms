

def nearest_zero(mat):
    row = len(mat)
    col =len(mat[0])
    result =[[None]*col for i in range(row)]

    for i in range(row):
        for j in range(col):
            result[i][j] =999999999999

    # print(result)
    for i in range(row):
        for j in range(col):
            for k in range(row):
                for l in range(col):
                    if(mat[k][l] ==0):
                        result[i][j] =min(result[i][j],(abs(i-k)+abs(j-l)))


    print(result)

# mat = [[0, 0, 0, 1],
#        [0, 0, 1, 1],
#        [0, 1, 1, 0]]
mat=[[0,0],[0,1],[1,1]]
nearest_zero(mat)