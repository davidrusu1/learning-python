import random as rd

def verify_matrix(mat):  # verifica daca o matrice 3x3 este buna pentru sudoku
    number = [0 for i in range(10)]
    for i in range(3):
        for j in range(3):
            number[mat[i][j]] += 1
    for i in range(1,10):
        if number[i] != 1:
            return False
    return True

def verify_line(mat, lin):  # verifica daca o linie din matricea 9x9 este corecta
    number = [0 for i in range(10)]
    for i in range(9):
            number[mat[lin][i]] += 1
    for i in range(1,10):
        if number[i] != 1:
            return False
    return True

def verify_column(mat, col):  # verifica daca o coloana din matricea 9x9 este corecta
    number = [0 for i in range(10)]
    for i in range(9):
            number[mat[i][col]] += 1
    for i in range(1,10):
        if number[i] != 1:
            return False
    return True

def verify_sudoku_matrix(mat):  # pune toate conditiile intr-o singura functie
    for i in range(3):
        for j in range(3):
            if verify_matrix(mat[i][j]) == False:
                return False
    for i in range(9):
        if verify_line(mat, i) == False or verify_column(mat,i) == False:
            return False
    return True     

for i in range(3):
    for j in range(3):
        print(mat[i][j])
    print("\n")
print(verify_sudoku_matrix(mat))