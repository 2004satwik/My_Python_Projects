import tkinter as tk
def ftc():
    fh=ent.get()
    cl=(5/9)* (float(fh) - 32)
    lbl2["text"]=f"{round(cl, 2)} \N{DEGREE CELSIUS}"
win=tk.Tk()
win.title("Fahrenheit-to-celsius_converter")
frm=tk.Frame(master=win)
ent=tk.Entry(master=frm,width=10)
lbl=tk.Label(master=frm,text="\N{DEGREE FAHRENHEIT}")
ent.grid(row=0,column=0,sticky='e')
lbl.grid(row=0,column=1,sticky='w')
bun=tk.Button(master=win,text="convert",command=ftc)
lbl2=tk.Label(master=win,text='\N{DEGREE CELSIUS}')
frm.grid(row=0,column=0,padx=10)
bun.grid(row=0,column=1,pady=10)
lbl2.grid(row=0,column=2,padx=10)
win.mainloop()
