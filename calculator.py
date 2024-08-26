from tkinter import *
from math import sqrt

global flag
flag = False

root = Tk()
root.geometry("450x490") 
root.title("Calculator using GUI") 
root.configure(bg="white")
screen = StringVar()
screen.set("")
sc = Entry(root, text = screen, bg="black", fg = "lavender", font= "arial 30 bold")
sc.pack(fill='x')


def backspace () :
    global flag
    if flag == True :
        clear()
        flag = False
    l = list(screen.get())
    n = len(l)
    if screen.get() == 'sqrt' or l[n-1] == 't':
        l.remove('s')
        l.remove('q')
        l.remove('r')
        l.remove('t')
        s = ''.join(str(x) for x in l)
        screen.set(str(s))
        flag = False
        return
    l = l[:-1]
    s = ''.join(str(x) for x in l)
    screen.set(str(s))

def clear() :
    screen.set("")

def clickonbuttons (event) :
    global flag
    if flag == True :
        clear()
        flag = False
    screen.set(screen.get() + event.widget.cget('text'))

def equal () :
    global flag
    try :
       total = str(eval(sc.get()))
       screen.set(total)
    except :
        screen.set("Syntax Error")
        flag = True
        

f = Frame(root,bg="white")
b = Button(f,fg="black", text='1', font="arial 20",height=2,width=5)
b.pack(side=LEFT)#,padx=15)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text='2', font="arial 20",height=2,width=5)
b.pack(side=LEFT)#,padx=15)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text='3', font="arial 20",height=2,width=5)
b.pack(side=LEFT)#,padx=15)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text='C', font="arial 20",height=2,width=5,command=backspace)
b.pack(side=LEFT)
b.pack(side=LEFT)
f.pack()
b = Button(f,fg="black", text="AC", font="arial 20",command=clear,height=2,width=5)
b.pack(side=LEFT)
f.pack()


f = Frame(root,bg="white")
b = Button(f,fg="black", text='4', font="arial 20",height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text='5', font="arial 20",height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text='6', font="arial 20",height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text='+', font="arial 20",height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text='-', font="arial 20",height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()


f = Frame(root,bg="white")
b = Button(f,fg="black", text='7', font="arial 20",height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text='8', font="arial 20",height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text='9', font="arial 20",height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text='*', font="arial 20",height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text='/', font="arial 20",height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()


f = Frame(root,bg="white")
b = Button(f,fg="black", text='0', font="arial 20",height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text='.', font="arial 20",height=2,width=5)#
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text='%', font="arial 20",height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text='(', font="arial 20",height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text=')', font="arial 20",height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()


f = Frame(root,bg="white")
b = Button(f,fg="black", text="=", font="arial 20",height=2,width=17,command=equal)
b.pack(side=LEFT)
f.pack()
b = Button(f,fg="black", text='sqrt', font="arial 20",height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()
b = Button(f,fg="black", text='**', font="arial 20", height=2,width=5)
b.pack(side=LEFT)
b.bind('<Button-1>',clickonbuttons)
f.pack()


root.mainloop()
