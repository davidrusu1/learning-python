from tkinter import *
import tkinter as tk

count = 0

def par_impar():
    global count
    if count % 2 == 0:
        print("Numar par")
    else:
        print("Numar impar")
    count += 1

window = Tk() # instantiaza prima fereastra a interfetei grafice

window.geometry("1024x768")
window.title("Sudoku checker")

icon = PhotoImage(file="/mnt/c/Users/david/OneDrive/Desktop/Python/learning-python/sudokuLogo.png")

window.iconphoto(True, icon)
window.config(background = "#c1edca")

label = tk.Label(window, 
                text="Sudoku Checker:",
                font = ('Roman', 25, 'bold'),
                bg="#c1edca",
                relief=RAISED,
                bd = 4,
                padx = 5,
                pady = 5)

label.pack(padx = 0, pady = 10)

button = Button(window,
                text = 'Check!',
                font = ('Roman', 8, 'bold'),
                bg = "#c1edca",
                relief = "solid",
                bd = 1)
button.config(command = par_impar) # face functia cand apas pe click
button.place(relx = 0.5, rely = 0.99, anchor = "s")

window.mainloop()  # ne apara prima fereastra pe pc si se uita la evenimente

