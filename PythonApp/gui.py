from tkinter import *

window = Tk() # instantiaza prima fereastra a interfetei grafice

window.geometry("1024x768")
window.title("Sudoku checker")

icon = PhotoImage(file="/mnt/c/Users/david/OneDrive/Desktop/Python/learning-python/sudokuLogo.png")

window.iconphoto(True, icon)
window.mainloop()  # ne apara prima fereastra pe pc si se uita la evenimente

