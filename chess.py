def queen(n: int):
    matrix = [[0]*n for _ in range(n)]
    diagonal = set()
    contr_diagonal = set()
    column = set()
    matrix_list = []

    def recurs(r):
        if r == n:
            copy = [row.copy() for row in matrix]
            matrix_list.append(copy)
            return

        for i in range(n):
            if i in column or i-r in diagonal or i+r in contr_diagonal:
                continue
            column.add(i)
            diagonal.add(i-r)
            contr_diagonal.add(i+r)
            matrix[r][i] = 1
            recurs(r+1)

            column.remove(i)
            diagonal.remove(i-r)
            contr_diagonal.remove(i+r)
            matrix[r][i] = 0
    recurs(0)
    for i in matrix_list:
        for x in i:
            print(x)
        print()
    return len(matrix_list)


def rook(n: int):
    matrix = [[0]*n for _ in range(n)]
    column = set()
    matrix_list = []

    def recurs(r):
        if r == n:
            copy = [row.copy() for row in matrix]
            matrix_list.append(copy)
            return

        for i in range(n):
            if i in column:
                continue
            column.add(i)
            matrix[r][i] = 1
            recurs(r+1)

            column.remove(i)
            matrix[r][i] = 0
    recurs(0)

    return len(matrix_list)


def bishop(n:int):
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
            
    return len(matrix_list)




def knight(n: int):
    matrix = [[0]*n for _ in range(n)]
    possible = 0  # how many knights u can place in n to n matrix
    attacked_cells = 0
    unattacked_cells = n*n
    variations = 1
    for i in range(n):
        for j in range(n):

            if matrix[i][j] == 1:
                continue
            possible += 1
            a = i-2
            b1 = j-1
            b2 = j+1
            try:  # check upper left
                if a < 0:
                    raise IndexError()
                if b1 < 0:
                    raise IndexError()
                if matrix[a][b1] != 1:
                    attacked_cells += 1
                matrix[a][b1] = 1
            except:
                pass

            try:  # check upper right
                if a < 0:
                    raise IndexError()
                if b2 < 0:
                    raise IndexError()
                if matrix[a][b2] != 1:
                    attacked_cells += 1
                matrix[a][b1] = 1
            except:
                pass

            a = i+2
            b1 = j-1
            b2 = j+1

            try:  # check down left
                if a < 0:
                    raise IndexError()
                if b1 < 0:
                    raise IndexError()
                if matrix[a][b1] != 1:
                    attacked_cells += 1
                matrix[a][b1] = 1
            except:
                pass

            try:  # check down right
                if a < 0:
                    raise IndexError()
                if b2 < 0:
                    raise IndexError()
                if matrix[a][b2] != 1:
                    attacked_cells += 1
                matrix[a][b1] = 1
            except:
                pass

            a = i+1
            a1 = i-1
            b = j+2

            try:  # check right up
                if a < 0:
                    raise IndexError()
                if b < 0:
                    raise IndexError()
                if matrix[a][b] != 1:
                    attacked_cells += 1
                matrix[a][b] = 1
            except:
                pass

            try:  # check right down
                if a1 < 0:
                    raise IndexError()
                if b < 0:
                    raise IndexError()
                if matrix[a1][b] != 1:
                    attacked_cells += 1
                matrix[a1][b] = 1
            except:
                pass

            a = i+1
            a1 = i-1
            b = j-2

            try:  # check left up
                if a < 0:
                    raise IndexError()
                if b < 0:
                    raise IndexError()
                if matrix[a][b] != 1:
                    attacked_cells += 1
                matrix[a][b] = 1
            except:
                pass

            try:  # check left down
                if a1 < 0:
                    raise IndexError()
                if b < 0:
                    raise IndexError()
                if matrix[a1][b] != 1:
                    attacked_cells += 1
                matrix[a1][b] = 1
            except:
                pass

            variations *= unattacked_cells
            unattacked_cells -= attacked_cells
            if unattacked_cells <= 0:
                return variations
            if possible >= n:
                return variations

    if possible < n:
        return 0
    return variations
