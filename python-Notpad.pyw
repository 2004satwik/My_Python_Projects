import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
def ofile():
    fp=askopenfilename(
    filetypes=[("Text Files", "*.txt"),("All Files", "*.*")]
    )
    if not fp:
        return
    textbox.delete(1.0, tk.END)
    with open(fp, "r") as way:
        text=way.read()
        textbox.insert(tk.END, text)
        win.title(f"Python Notpad - {fp}")
def sfile():
    fp=asksaveasfilename(
    filetypes=[("text file", '*.txt'),("All files" '*.*')]
    )
    if not fp:
        return
    with open(fp, 'w') as gout:
        text=textbox.get(1.0, tk.END)
        gout.write(text)
        win.title(f"Python Notpad - {fp}")


def nfile():
    def dall():
        textbox.delete(1.0, tk.END)
        won.destroy()
    won=tk.Tk()
    won.title('WARNING')
    lbl=tk.Label(text="file may have not been saved!.Ignore if saved.",master=won)
    lbl.pack(side=tk.TOP)
    f2=tk.Frame(master=won)
    b1=tk.Button(text="save",master=f2,command=sfile)
    b2=tk.Button(text="Ignore",master=f2,command=dall)
    b1.grid(row=0,column=0,sticky="ew")
    b2.grid(row=0,column=1,sticky="ew")
    f2.pack(side=tk.TOP)


win=tk.Tk()
win.rowconfigure(0, minsize=700,weight=1)
win.columnconfigure(1, minsize=700,weight=1)
frm=tk.Frame(master=win)
sbun=tk.Button(text="Save as..",master=frm,bg="light grey",command=sfile)
obun=tk.Button(text="open",master=frm,bg="light grey",command=ofile)
nbun=tk.Button(text="New", master=frm,bg='light grey',command=nfile)
sbun.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
obun.grid(row=1,column=0,sticky="ew",padx=5,pady=5)
nbun.grid(row=2,column=0,sticky="ew",padx=5,pady=5)
textbox=tk.Text(master=win)
textbox.grid(row=0,column=1,sticky="nsew")
frm.grid(row=0,column=0,sticky="ns")
win.mainloop()


