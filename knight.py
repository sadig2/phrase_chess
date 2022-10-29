
n = 3

def bishop(n:int):
    perm = 0
    matrix = [[0]*n for _ in range(n)]
    diag = set()
    non_diag = set()
    matrix_list = []
    def recurs(row ,column, count):
        if count == 0:
            matrix_list.append([i.copy() for i in matrix])
            return # leave the last function
        if column >= n:
            recurs(row+1, 0, count)
            return
        if row == n :
            return
    
        if column-row not in diag and column+row not in non_diag:
            matrix[row][column] = 1
            diag.add(column-row)
            non_diag.add(column+row)
            recurs(row, column + 1, count-1)
            matrix[row][column] = 0
            diag.remove(column-row)
            non_diag.remove(column+row)
        recurs(row, column + 1, count)

    recurs(0,0,n)
            
    return matrix_list




l = bishop(n)

for i in l:
    for k in i:
        print(k)
    print()
