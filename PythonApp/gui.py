from tkinter import *
import tkinter as tk

class SudokuCheckerGUI:
    def __init__(self, window, func):
        self.window = window
        self.func = func
        self.window.geometry("600x500")
        self.window.title("Sudoku Checker:")
        self.window.config(background = "#c1edca")

        # Icon for App
        try:
            icon = PhotoImage(file="/mnt/c/Users/david/OneDrive/Desktop/Python/learning-python/sudokuLogo.png")
            self.window.iconphoto(True, icon)
        except Exception:
            pass
        
        # Variable for saving values
        self.matrix = []

        # Title
        self.label = Label(window,
                           text="Sudoku Checker:",
                           font=('Roman', 25, 'bold'),
                           bg="#c1edca",
                           relief=RAISED,
                           bd=4,
                           padx=5,
                           pady=5)
        self.label.pack(padx=0, pady=10)

        # Frame for having a table inside
        self.frame = Frame(window,
                           bg = 'black',
                           width = 100,
                           height = 200)
        self.frame.pack(padx = 10, pady = 10)

        # Input validation
        vcmd = (self.frame.register(self.limit_one_character), '%P')

        # 9x9 Matrix
        for i in range(9):
            matrixRow = []
            for j in range(9):
                e = Entry(self.frame,
                          validate='key',
                          validatecommand=vcmd,
                          width=4,
                          fg='blue',
                          font=('Arial', 16, 'bold'),
                          justify='center',
                          bd=2)
                e.grid(row=i, column=j)
                e.bind('<KeyRelease>', lambda event, x=i, y=j: self.muta_focus(event, x, y))
                matrixRow.append(e)
            self.matrix.append(matrixRow)
        
        # Button Check
        self.button = Button(window,
                             text='Check!',
                             font=('Roman', 8, 'bold'),
                             bg="#c1edca",
                             activebackground="#56e773",
                             relief="solid",
                             bd=1,
                             command=self.check)
        self.button.place(relx=0.5, rely=0.99, anchor="s")
    
    def limit_one_character(self, text):
        return text == "" or (len(text) <= 1 and text.isdigit())
    
    def get_matrix_values(self):
        mat = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.matrix[i][j].get()
                if val.isdigit():
                    row.append(int(val))
                else:
                    row.append(0)  # pentru celulele goale sau invalide
            mat.append(row)
        return mat

    def check(self):
        matrice_valori = self.get_matrix_values()
        if self.func(matrice_valori):
            print("Sudoku este valid")
        else:
            print("Sudoku este gresit")

    def muta_focus(self, event, i, j):
        if len(event.widget.get()) == 1:
            if j < 8:
                self.matrix[i][j + 1].focus_set()
            elif i < 8:
                self.matrix[i + 1][0].focus_set()



