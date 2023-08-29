import tkinter as tk
from tkinter import PhotoImage
from tkinter.filedialog import asksaveasfilename
n=0
z=0
lst1=[]

def DC():
    import cartooncats
    cartooncats

def NC():
    global n
    n=n+1
def PC():
    global n
    n=n-1
def fs(): #yet to be completed (incomplete)
    sfil=asksaveasfilename(
    filetypes=[("image file", '*.png'),("All files", '*.*')]
    )
    if not sfil:
        return
    #with open(sfil, 'w') as getout:
        #getout.write(lbl)

def BCOUNT():
    global z
    z=2

def YCOUNT():
    global z
    z=3

def WCOUNT():
    global z
    z=4

def BRCOUNT():
    global z
    z=5

def GCOUNT():
    global z
    z=6

def DGCOUNT():
    global z
    z=7

def GRCOUNT():
    global z
    z=8

def OCOUNT():
    global z
    z=9

def nBLACK():
    global lst1
    global n
    lst1=['Timepass','\BLACK\B1.png','\BLACK\B2.png','\BLACK\B3.png','\BLACK\B4.png','\BLACK\B5.png','\BLACK\B6.png','\BLACK\B7.png','\BLACK\B8.png','\BLACK\B9.png','\BLACK\B10.png']
    if n==0:n=10
    elif n==11:n=1

def nYELLOW():
    global lst1
    global n
    lst1=['Timepass','\YELLOW\Y1.png','\YELLOW\Y2.png','\YELLOW\Y3.png','\YELLOW\Y4.png','\YELLOW\Y5.png','\YELLOW\Y6.png','\YELLOW\Y7.png','\YELLOW\Y8.png','\YELLOW\Y9.png','\YELLOW\Y10.png','\YELLOW\Y11.png','\YELLOW\Y12.png','\YELLOW\Y13.png','\YELLOW\Y14.png','\YELLOW\Y15.png','\YELLOW\Y16.png','\YELLOW\Y17.png','\YELLOW\Y18.png']
    if n==0:n=18
    elif n==19:n=1

def nWHITE():
    global lst1
    global n
    lst1=['Timepass','\WHITE\W1.png','\WHITE\W2.png','\WHITE\W3.png','\WHITE\W4.png','\WHITE\W5.png','\WHITE\W6.png','\WHITE\W7.png','\WHITE\W8.png','\WHITE\W9.png','\WHITE\W10.png','\WHITE\W11.png','\WHITE\W12.png']
    if n==0:n=12
    elif n==13:n=1

def nBROWN():
    global lst1
    global n
    lst1=['Timepass','\BROWN\BR1.png','\BROWN\BR2.png','\BROWN\BR3.png','\BROWN\BR4.png','\BROWN\BR5.png','\BROWN\BR6.png','\BROWN\BR7.png','\BROWN\BR8.png','\BROWN\BR9.png','\BROWN\BR10.png','\BROWN\BR11.png']
    if n==0:n=11
    elif n==12:n=1

def nGREY():
    global lst1
    global n
    lst1=['Timepass','\GREY\G1.png','\GREY\G2.png','\GREY\G3.png','\GREY\G4.png','\GREY\G5.png','\GREY\G6.png','\GREY\G7.png']
    if n==0:n=7
    elif n==8:n=1

def nDGREY():
    global lst1
    global n
    lst1=['Timepass','\DGREY\DG1.png','\DGREY\DG2.png','\DGREY\DG3.png','\DGREY\DG4.png','\DGREY\DG5.png','\DGREY\DG6.png','\DGREY\DG7.png','\DGREY\DG8.png','\DGREY\DG9.png']
    if n==0:n=9
    elif n==10:n=1

def nGREEN():
    global lst1
    global n
    lst1=['Timepass','\GREEN\GRE1.png','\GREEN\GRE2.png','\GREEN\GRE3.png','\GREEN\GRE4.png','\GREEN\GRE5.png','\GREEN\GRE6.png','\GREEN\GRE7.png','\GREEN\GRE8.png','\GREEN\GRE9.png','\GREEN\GRE10.png','\GREEN\GRE11.png','\GREEN\GRE12.png']
    if n==0:n=1
    elif n==2:n=1

def nORANGE():
    global lst1
    global n
    lst1=['Timepass','\ORANGE\O1.png','\ORANGE\O2.png','\ORANGE\O3.png','\ORANGE\O4.png','\ORANGE\O5.png','\ORANGE\O6.png']
    if n==0:n=6
    elif n==7:n=1

def LC():
    global z
    global lst1
    global win
    win1=tk.Toplevel()
    win1.attributes('-fullscreen',True)
    win1.title("Black cats")
    SFrame=tk.Frame(master=win1,width=80)
    SFrame.pack(side=tk.TOP)
    SBUN=tk.Button(master=SFrame,text="SAVE",bg="yellow",command=fs)
    SBUN.pack(side=tk.LEFT,anchor='nw')
    if z==2:
        nBLACK()
    elif z==3:
        nYELLOW()
    elif z==4:
        nWHITE()
    elif z==5:
        nBROWN()
    elif z==6:
        nGREY()
    elif z==7:
        nDGREY()
    elif z==8:
        nGREEN()
    elif z==9:
        nORANGE()
    else:
        print("none")
    Bn=lst1[n]
    print(Bn)
    dire=("G:\python\cats\_appdata_"+Bn)
    poto1=PhotoImage(file=dire)
    lbl=tk.Label(master=win1,bg="dark blue", image=poto1)
    lbl.pack(side=tk.TOP)
    BFRM=tk.Frame(master=win1,width=80)
    BFRM.pack(side=tk.TOP)
    NBUN=tk.Button(master=BFRM,text="NEXT>>",bg="pink",command=lambda:[NC(),LC()])
    PBUN=tk.Button(master=BFRM,text="<<PREVIOUS",bg="pink",command=lambda:[PC(),LC()])
    CBUN=tk.Button(master=SFrame,text="CLOSE",bg="pink",command=lambda:[win.destroy(),DC()])
    CBUN.pack(side=tk.LEFT,anchor='nw')
    NBUN.pack(side=tk.RIGHT,anchor='ne')
    PBUN.pack(side=tk.LEFT,anchor='nw')
    win1.mainloop()


class cats:
    def __init__(self,color):
        self.color=color
win=tk.Tk()
win.title("cartoon cats")
f1=tk.Frame(master=win,bg="grey",width=80)
f1.pack(side=tk.TOP)
L1=tk.Label(master=f1,text="welcome to  CARTOON_CATS!",font="times 16 bold",bg="grey")
L1.pack(side=tk.TOP,fill=tk.BOTH,pady=10)
L2=tk.Label(master=f1,text="choose a colour for your cat:",fg="orange",bg="grey")
L2.pack(side=tk.TOP,fill=tk.BOTH)
f2=tk.Frame(master=win,width=80)
f2.pack(side=tk.TOP)
BBUN=tk.Button(master=f2,text="BLACK",fg='black',bg="sky blue",width=80,command=lambda:[BCOUNT(),LC()])
BBUN.pack(side=tk.TOP,pady=5)
YBUN=tk.Button(master=f2,text="YELLOW",fg='black',bg="sky blue",width=80,command=lambda:[YCOUNT(),LC()])
YBUN.pack(side=tk.TOP)
WBUN=tk.Button(master=f2,text="WHITE",fg='black',bg="sky blue",width=80,command=lambda:[WCOUNT(),LC()])
WBUN.pack(side=tk.TOP,pady=5)
BRBUN=tk.Button(master=f2,text="BROWN",fg='black',bg="sky blue",width=80,command=lambda:[BRCOUNT(),LC()])
BRBUN.pack(side=tk.TOP)
GBUN=tk.Button(master=f2,text="GREY",fg='black',bg="sky blue",width=80,command=lambda:[GCOUNT(),LC()])
GBUN.pack(side=tk.TOP,pady=5)
DGBUN=tk.Button(master=f2,text="DARK GREY",fg='black',bg="sky blue",width=80,command=lambda:[DGCOUNT(),LC()])
DGBUN.pack(side=tk.TOP)
GRBUN=tk.Button(master=f2,text="GREEN",fg='black',bg="sky blue",width=80,command=lambda:[GRCOUNT(),LC()])
GRBUN.pack(side=tk.TOP,pady=5)
OBUN=tk.Button(master=f2,text="ORANGE",fg='black',bg="sky blue",width=80,command=lambda:[OCOUNT(),LC()])
OBUN.pack(side=tk.TOP)
win.mainloop()

#THONK YOU
#CODE SATWIK
