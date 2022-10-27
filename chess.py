def queen(n: int):
    if n == 1:
        return 1
    matrix = [[0]*n for _ in range(n)]
    possible = 0  # how many queens u can place in n to n matrix
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                continue
            possible += 1
            for x in range(n):
                matrix[i][x] = 1
                matrix[x][j] = 1
                try:
                    matrix[i+x][j+x] = 1
                except:
                    print("index out of range")

                try:
                    matrix[i-x][j-x] = 1
                except:
                    print("index out of range")
                try:
                    matrix[i+x][j-x] = 1
                except:
                    print("index out of range")

                try:
                    matrix[i-x][j+x] = 1
                except:
                    print("index out of range")

    if possible < n:
        return 0


def rook(n: int) -> int:
    matrix = [[0]*n for _ in range(n)]
    possible = 0  # how many rooks u can place in n to n matrix
    attacked_cells = 0
    unattacked_cells = n*n
    variations = 1
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                continue
            possible += 1
            for x in range(n):
                if matrix[i][x] != 1:
                    attacked_cells += 1
                    matrix[i][x] = 1
                if matrix[x][j] != 1:
                    attacked_cells += 1
                    matrix[x][j] = 1
            variations *= unattacked_cells
            unattacked_cells -= attacked_cells
            if unattacked_cells <= 0:
                return variations
            if possible >= n:
                return variations

    if possible < n:
        return 0
    return variations


def bishop(n: int):
    matrix = [[0]*n for _ in range(n)]
    possible = 0  # how many bishops u can place in n to n matrix
    attacked_cells = 0
    unattacked_cells = n*n
    variations = 1
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                continue
            possible += 1
            for x in range(n):
                try:
                    if matrix[i+x][j+x] != 1:
                        attacked_cells += 1
                    matrix[i+x][j+x] = 1
                except:
                    print("index out of range")
                try:
                    a = i-x
                    if a < 0:
                        raise IndexError()
                    b = j-x
                    if b < 0:
                        raise IndexError()
                    if matrix[a][b] != 1:
                        attacked_cells += 1
                    matrix[a][b] = 1
                except:
                    print("index out of range")
                try:
                    b = j-x
                    if b < 0:
                        raise IndexError()
                    if matrix[i+x][b] != 1:
                        attacked_cells += 1
                    matrix[i+x][b] = 1
                except:
                    print("index out of range")

                try:
                    a = i-x
                    if a < 0:
                        raise IndexError()
                    if matrix[a][j+x] != 1:
                        attacked_cells += 1
                    matrix[a][j+x] = 1
                except:
                    print("index out of range")
            variations *= unattacked_cells
            unattacked_cells -= attacked_cells
            if unattacked_cells <= 0:
                return variations
            if possible >= n:
                return variations

    if possible < n:
        return 0
    return variations


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
                print("index out of range")

            try:  # check upper right
                if a < 0:
                    raise IndexError()
                if b2 < 0:
                    raise IndexError()
                if matrix[a][b2] != 1:
                    attacked_cells += 1
                matrix[a][b1] = 1
            except:
                print("index out of range")

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
                print("index out of range")

            try:  # check down right
                if a < 0:
                    raise IndexError()
                if b2 < 0:
                    raise IndexError()
                if matrix[a][b2] != 1:
                    attacked_cells += 1
                matrix[a][b1] = 1
            except:
                print("index out of range")

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
                print("index out of range")

            try:  # check right down
                if a1 < 0:
                    raise IndexError()
                if b < 0:
                    raise IndexError()
                if matrix[a1][b] != 1:
                    attacked_cells += 1
                matrix[a1][b] = 1
            except:
                print("index out of range")

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
                print("index out of range")

            try:  # check left down
                if a1 < 0:
                    raise IndexError()
                if b < 0:
                    raise IndexError()
                if matrix[a1][b] != 1:
                    attacked_cells += 1
                matrix[a1][b] = 1
            except:
                print("index out of range")

            variations *= unattacked_cells
            unattacked_cells -= attacked_cells
            if unattacked_cells <= 0:
                return variations
            if possible >= n:
                return variations

    if possible < n:
        return 0
    return variations
