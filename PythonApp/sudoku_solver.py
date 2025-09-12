import random as rd
from gui import SudokuCheckerGUI
from tkinter import *
import tkinter as tk

def verify_matrix(mat):  # verifica daca o matrice 3x3 este buna pentru sudoku
    number = [0 for i in range(10)]
    for i in range(3):
        for j in range(3):
            if mat[i][j] < 1 or mat[i][j] > 9:
                return False
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
    for i in range(9):
        if verify_line(mat, i) == False or verify_column(mat, i) == False:
            return False
    for i in range(3):
        for j in range(3):
            bloc = [row[(j*3):(j*3)+3] for row in mat[(i*3):(i*3)+3]]
            if not verify_matrix(bloc):
                return False
    return True
# Matricea trebuie sa fie de genul 9x9 vector de vector practic

def main():
    window = Tk()
    gui = SudokuCheckerGUI(window, verify_sudoku_matrix)
    window.mainloop()


if __name__ == '__main__':
    main()