from tkinter import *
import tkinter as tk

# Functii

def par_impar():
    global count
    if count % 2 == 0:
        print(f"Ai apasat de {count}, care este un numar par.")
    else:
        print(f"Ai apasat de {count}, care este un numar impar.")
    count += 1

def limit_one_character(text):
    return text == "" or (len(text) <= 1 and text.isdigit())

def citeste_valori():
    tabla = []
    for i in range(9):
        rand = []
        for j in range(9):
            valoare = matrice[i][j].get()
            rand.append(valoare)
        tabla.append(rand)
    print(tabla)


def muta_focus(event, i, j):
    if len(event.widget.get()) == 1:
        if j < 8:
            matrice[i][j+1].focus_set()
        elif i < 8:
            matrice[i+1][0].focus_set()


# Variabile
count = 0
matrice = []
window = Tk() # instantiaza prima fereastra a interfetei grafice

window.geometry("600x500")
window.title("Sudoku checker")

icon = PhotoImage(file="/mnt/c/Users/david/OneDrive/Desktop/Python/learning-python/sudokuLogo.png")

window.iconphoto(True, icon)
window.config(background = "#c1edca")

label = Label(window, 
                text="Sudoku Checker:",
                font = ('Roman', 25, 'bold'),
                bg="#c1edca",
                relief=RAISED,
                bd = 4,
                padx = 5,
                pady = 5)

label.pack(padx = 0, pady = 10)

frame = Frame(window, bg = 'blue', width = 100, height = 200)
frame.pack(padx = 10, pady = 10)

vcmd = (frame.register(limit_one_character), '%P')

for i in range(9):
    rand = []
    for j in range(9):
        e = Entry(frame, validate = 'key',
                validatecommand = vcmd,
                width = 4,
                fg = 'blue',
                font = ('Arial', 16, 'bold'),
                justify = 'center',
                bd = 2)
        e.grid(row = i, column = j)
        e.bind('<KeyRelease>', lambda event, x=i, y=j: muta_focus(event, x, y))
        rand.append(e)
    matrice.append(rand)

button = Button(window,
                text = 'Check!',
                font = ('Roman', 8, 'bold'),
                bg = "#c1edca",
                activebackground = "#56e773",
                relief = "solid",
                bd = 1)
button.config(command = citeste_valori) # face functia cand apas pe click
button.place(relx = 0.5, rely = 0.99, anchor = "s")

window.mainloop()  # ne apara prima fereastra pe pc si se uita la evenimente

