import tkinter as tk
window=tk.Tk()
board={"sunkden":tk.SUNKEN,"groove":tk.GROOVE,'raised':tk.RAISED}
for a,b in board.items():
    frame=tk.Frame(master=window ,relief=b, borderwidth=6)
    frame.pack(side=tk.LEFT)
    label=tk.Label(master=frame, text=a)
    label.pack()
window.mainloop()
