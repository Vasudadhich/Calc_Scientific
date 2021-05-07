from tkinter import *
import time
root=Tk()
root.title('Calc')
root.config(bg='red')
root.geometry("500x600")
def Result(x):
    if x=='=':
        try:
            string.set(eval(string.get()))
        except Exception as e:
            string.set(e)
    elif x=='C':
        string.set('')
    elif x=='CE':
        string.set(string.get()[:-1])
    else:
        string.set(string.get()+x)



string=StringVar()
e1=Entry(root,textvariable=string,font="arial 20 bold",bg='powder blue',justify=RIGHT,relief=RAISED)
e1.grid(row=0,column=0,columnspan=4,padx=10,pady=10,sticky='nswe')
i=1
for data in ['789/','456*','123+','.0=-',['C','CE']]:
    j=0
    for d in data:
        b=Button(root,text=d,font="arial 20 bold",bg='powder blue',
                 command=lambda x=d:Result(x),relief=RAISED)
        if d in ['C','CE']:
            b.grid(row=i,column=j,padx=10,pady=10,sticky='nswe',columnspan=2)
            j+=2
        else:
            b.grid(row=i,column=j,padx=10,pady=10,sticky='nswe')
            j+=1
    i+=1
def ShowTime():
    label['text']=time.ctime()
    label.after(1000,ShowTime)

label=Label(root,font="arial 20 bold",bg='powder blue',relief=RAISED)
label.grid(row=6,column=0,sticky='nswe',columnspan=4,padx=10,pady=10)
ShowTime()
b=Button(root,text='Close',font="arial 20 bold",bg='powder blue',
         command=lambda:root.destroy(),relief=RAISED)
b.grid(row=7,column=0,sticky='nswe',columnspan=4,padx=10,pady=10)
for i in range(8):
    root.grid_rowconfigure(i,weight=1)
for i in range(4):
    root.grid_columnconfigure(i,weight=1)
root.mainloop()
