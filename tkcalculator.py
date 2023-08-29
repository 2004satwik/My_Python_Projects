import tkinter as tk
win=tk.Tk()
win.title('python-Calculator')
f1=tk.Frame(master=win,bg='sky blue',relief=tk.RIDGE)
e1=tk.Entry(master=f1,width=20)
e1.pack(pady=5,fill=tk.BOTH)
f1.pack(side=tk.TOP,fill=tk.BOTH)
frm=tk.Frame(master=win)

def sol():
    try:
        s=e1.get()
        ad='+' in s
        su='-' in s
        mu='*' in s
        di='/' in s
        pe='%' in s
        if ad:
            lol=s.split('+')
            x=float(lol[0])
            y=float(lol[1])
            z=x+y
            e1.delete(0, tk.END)
            e1.insert(tk.END,z)
        if mu:
            lol = s.split('*')
            x = float(lol[0])
            y = float(lol[1])
            z = x * y
            e1.delete(0, tk.END)
            e1.insert(tk.END, z)
        if su:
            lol = s.split('-')
            x = float(lol[0])
            y = float(lol[1])
            z = x - y
            e1.delete(0, tk.END)
            e1.insert(tk.END, z)
        if di:
            lol = s.split('/')
            x = float(lol[0])
            y = float(lol[1])
            z = x / y
            e1.delete(0, tk.END)
            e1.insert(tk.END, z)
        if pe:
            lol = s.split('%')
            x = float(lol[0])
            y = float(lol[1])
            l = x * y
            z=l/100
            e1.delete(0, tk.END)
            e1.insert(tk.END, z)
    except:
        e1.delete(0, tk.END)
        b=('Error')
        e1.insert(0, b)


def dele():
    e1.delete(0,tk.END)

def nu7():
    val7=7
    e1.insert(tk.END,val7)
bun7=tk.Button(text=" 7 ",master=frm,bg='light green',command=nu7)
def nu8():
    val8=8
    e1.insert(tk.END,val8)
bun8=tk.Button(text=" 8 ",master=frm,bg='light green',command=nu8)
def nu9():
    val9=9
    e1.insert(tk.END,val9)
bun9=tk.Button(text=" 9 ",master=frm,bg='light green',command=nu9)
def nu4():
    val4=4
    e1.insert(tk.END,val4)
bun4=tk.Button(text=" 4 ",master=frm,bg='light green',command=nu4)
def nu5():
    val5=5
    e1.insert(tk.END,val5)
bun5=tk.Button(text=" 5 ",master=frm,bg='light green',command=nu5)
def nu6():
    val6=6
    e1.insert(tk.END,val6)
bun6=tk.Button(text=" 6 ",master=frm,bg='light green',command=nu6)
def nu1():
    val1=1
    e1.insert(tk.END,val1)
bun1=tk.Button(text=" 1 ",master=frm,bg='light green',command=nu1)
def nu2():
    val2=2
    e1.insert(tk.END,val2)
bun2=tk.Button(text=" 2 ",master=frm,bg='light green',command=nu2)
def nu3():
    val3=3
    e1.insert(tk.END,val3)
bun3=tk.Button(text=" 3 ",master=frm,bg='light green',command=nu3)
def nu0():
    val0=0
    e1.insert(tk.END,val0)
bun0=tk.Button(text=" 0 ",master=frm,bg='light green',command=nu0)
def nu00():
    val00='00'
    e1.insert(tk.END,val00)
bun00=tk.Button(text="00",master=frm,bg='light green',command=nu00)
def dot():
    valdot='.'
    e1.insert(tk.END,valdot)
bun=tk.Button(text=" . ",master=frm,bg='light green',command=dot)
def div():
    valdiv='/'
    e1.insert(tk.END,valdiv)
bundiv=tk.Button(text=" / ",master=frm,bg='pink',command=lambda:[sol(), div()])
def mul():
    vmul = '*'
    e1.insert(tk.END, vmul)
bunmul=tk.Button(text=" x ",master=frm,bg='pink',command=lambda:[sol(),mul()])
def vad():
    e1.insert(tk.END, '+')
bunadd=tk.Button(text="+",master=frm,bg='pink',command=lambda:[sol(),vad()])
buneq=tk.Button(text=" = ",master=frm,bg='blue',fg='pink',command=sol)
def sub():
    valsub='-'
    e1.insert(tk.END,valsub)
bunsub=tk.Button(text=" - ",master=frm,bg='pink',command=lambda:[sol(),sub()])
def per():
    try:
        l = e1.get()
        dv = '/' in l
        if dv:
            lol = l.split('/')
            x = float(lol[0])
            y = float(lol[1])
            ab = x/y
            z= ab*100
            e1.delete(0, tk.END)
            e1.insert(tk.END, z)
        else:
            valper='%'
            e1.insert(tk.END,valper)
    except:
        e1.delete(0, tk.END)
        b = ('Error')
        e1.insert(0, b)

bunper=tk.Button(text=" % ",master=frm,bg='pink',command=per)
def rot():
    h=e1.get()
    f=float(h)
    l=(f)**0.5
    e1.delete(0, tk.END)
    e1.insert(tk.END, l)
bunro=tk.Button(text="ro ",master=frm,bg='pink',command=lambda:[sol(),rot()])
bundel=tk.Button(text="CE",master=frm,bg='red',command=dele)
def exi():
    win.destroy()
ex=tk.Button(master=win,width=20,text='Exit',bg='red',command=exi)
bun7.grid(row=0, column=0,sticky="nsew",padx=5,pady=5)
bun4.grid(row=1, column=0)
bun1.grid(row=2, column=0, pady=5)
bun0.grid(row=3, column=0)
bun8.grid(row=0, column=1,ipadx=1)
bun5.grid(row=1, column=1,ipadx=1)
bun2.grid(row=2, column=1,ipadx=1)
bun00.grid(row=3, column=1,ipadx=1.2)
bun9.grid(row=0, column=2,padx=5,ipadx=1)
bun6.grid(row=1, column=2,ipadx=0.5)
bun3.grid(row=2, column=2,ipadx=0.5)
bun.grid(row=3, column=2,ipadx=2.5)
bundiv.grid(row=0, column=3,ipadx=1)
bunmul.grid(row=1, column=3,ipadx=1.0)
bunadd.grid(row=2, column=3,ipadx=4.5)
bunsub.grid(row=3, column=3, ipadx=2)
bundel.grid(row=0, column=4,padx=5,ipadx=1)
bunper.grid(row=1, column=4)
bunro.grid(row=2, column=4,ipadx=1)
buneq.grid(row=3, column=4,ipadx=1.5)
frm.pack(side=tk.TOP, fill=tk.BOTH)
ex.pack(side=tk.TOP,pady=5)
win.mainloop()
