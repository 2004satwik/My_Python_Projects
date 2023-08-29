import tkinter as tk
window=tk.Tk()
def handle(even):
    print(even.char)
window.bind("<Key>", handle)
window.mainloop()
