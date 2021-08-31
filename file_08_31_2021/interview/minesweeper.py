

def mine_sweeper(bombs,n_row,n_col):
    field =[[0 for i in range(n_col)] for j in range(n_row)]

    for bomb_location in bombs:
        bomb_row,bomb_col =bomb_location
        field[bomb_row][bomb_col]=-1
        row_range = range(bomb_row-1,bomb_row+2)
        col_range = range(bomb_col-1,bomb_col+2)

        for i in row_range:
            current_i =i
            for j in col_range:
                current_j =j
                if (0 <= i < n_row and 0 <= j < n_col and field[i][j] != -1):
                    field[i][j] += 1
    return field



print(mine_sweeper([[0,0],[1,2]],3,4))