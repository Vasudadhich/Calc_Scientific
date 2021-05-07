from tkinter import *
import  math as m

font=('times',25)
win=Tk()
win.title('my calculator')
win.geometry('335x435')
headinglabel=Label(win,text='Calculator',font=font)
headinglabel.pack(pady=5)

value=StringVar()
value.set("")
def result(x):
    if x == '=':
        try:
            value.set(eval(value.get()))
        except Exception as e:
            value.set(e)
    elif x == 'C':
        value.set("")
    elif x == 'CE':
        value.set(value.get()[:-1])
    else:
        value.set(value.get() + x)



textfield=Entry(win,textvar=value,font=font,justify=RIGHT)
textfield.pack(padx=5,pady=5,fill=X)

buttonframe=Frame(win)
buttonframe.pack()
a=1
for i in range(0,3):
    for j in range(0,3):
        button=Button(buttonframe,text=a,font=font,relief='ridge',width=4,activebackground='orange',
                      activeforeground='white',command=lambda x=a:result(str(x)))
        button.grid(row=i,column=j)
        a=a+1
l=['.','0','=']
k=0
for i in l:
    button = Button(buttonframe, text=i, font=font, relief='ridge', width=4,activebackground='orange'
                    ,activeforeground='white',command=lambda x=i:result(x))
    button.grid(row=3, column=k)
    k+=1
l=['+','-','*','/']
k=0
for i in l:
    button = Button(buttonframe, text=i, font=font, relief='ridge', width=4,activebackground='orange',activeforeground='white',command=lambda x=i:result(x))
    button.grid(row=k, column=3)
    k+=1
l=['CE','C']
k=0
for i in l:
    button = Button(buttonframe, text=i, font=font, relief='ridge',activebackground='orange',activeforeground='white',command=lambda x=i:result(x))
    button.grid(row=4, column=k,columnspan=2,sticky='nswe')
    k+=2


def sciresult(x):
    if x=='√':
        value.set(m.sqrt(float(value.get())))
    elif x=='^':
        b,p=value.get().split(",")
        value.set(m.pow(int(b),int(p)))
    elif x=='x!':
        value.set(m.factorial(int(value.get())))
    elif x=='Rad':
        value.set(m.radians(float(value.get())))
    elif x=='Deg':
        value.set(m.degrees(float(value.get())))
    elif x=='Sin':
        value.set(m.sin(m.radians(float(value.get()))))
    elif x=='Cos':
        value.set(m.cos(m.radians(float(value.get()))))
    elif x=='Tan':
        value.set(m.tan(m.radians(float(value.get()))))
scframe=Frame(win)
l=[['√','^','x!','Rad'],['Deg','Sin','Cos','Tan']]
r=0
for i in l:
    c=0
    for i in i:
        sqrbutton = Button(scframe, text=i, font=font,width=4, command=lambda x=i:sciresult(x),
                           relief='ridge',activebackground='orange',activeforeground='white')
        sqrbutton.grid(row=r, column=c,sticky='nswe')
        c+=1
    r+=1



normcalc=True
def scicalci():
    global  normcalc
    if normcalc:
        buttonframe.pack_forget()
        scframe.pack(side=TOP,padx=3,pady=5)
        buttonframe.pack(side=TOP)
        win.geometry('335x570')
        normcalc=False
    else:
        scframe.pack_forget()
        normcalc=True
        win.geometry('335x435')



menubar=Menu(win,font=('times',20))
mode=Menu(menubar,tearoff=0,font=('times',15))
mode.add_checkbutton(label='Scientific Calculator',command=scicalci)
menubar.add_cascade(label='mode',menu=mode)
win.config(menu=menubar)

win.mainloop()
