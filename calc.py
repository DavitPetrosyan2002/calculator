from tkinter import *
from tkinter import Tk

win=Tk()
def add_digit(x):
    value=calc.get()
    if value[0]=='0':
        value=value[1:]
    calc.delete(0,END)
    calc.insert(0,value+x)

def add__operation(y):
    value=calc.get()
    if value[-1]=='+' or value[-1]=='-' or value[-1]=='/' or value[-1]=='*':
      value=value+value[::-1] 
    calc.delete(0,END)
    calc.insert(0,value+Y)

def clear():
    calc.delete(0,END)
    calc.insert(0,'0')


def calculate():
    value=calc.get()
    if value[-1] in '-+/*':
        value=value+value[:-1]
    calc.delete(0,END)
    calc.insert(0,eval(value))




def make_digit_button(x): 
    return Button(text=x,bd=5, command=lambda :add_digit(x))  

def make_operation_button(y): 
    return Button(text=y,bd=5, command=lambda :add_digit(y),fg='red') 

def make_calc_button(y): 
    return Button(text=y,bd=5, command=calculate,fg='red')   

def make_clear_button(y): 
    return Button(text=y,bd=5, command=clear,fg='red')         

win.title("calculator")
win.geometry("240x270+100+200")
win['bg']='#33ffe6'
calc=Entry(win,justify='right',font=('arial',15),width=15)
calc.insert(0,'0')
calc.grid(row=0,column=0,columnspan=4,stick='we',padx=5)
make_digit_button('1').grid(row=1,column=0, stick='wens',padx=5,pady=5)
make_digit_button('2').grid(row=1,column=1, stick='wens',padx=5,pady=5)
make_digit_button('3').grid(row=1,column=2, stick='wens',padx=5,pady=5)
make_digit_button('4').grid(row=2,column=0, stick='wens',padx=5,pady=5)
make_digit_button('5').grid(row=2,column=1, stick='wens',padx=5,pady=5)
make_digit_button('6').grid(row=2,column=2, stick='wens',padx=5,pady=5)
make_digit_button('7').grid(row=3,column=0, stick='wens',padx=5,pady=5)
make_digit_button('8').grid(row=3,column=1, stick='wens',padx=5,pady=5)
make_digit_button('9').grid(row=3,column=2, stick='wens',padx=5,pady=5)
make_digit_button('0').grid(row=4,column=0, stick='wens',padx=5,pady=5)

make_operation_button('+').grid(row=1,column=3, stick='wens',padx=5,pady=5)
make_operation_button('-').grid(row=2,column=3, stick='wens',padx=5,pady=5)
make_operation_button('/').grid(row=3,column=3, stick='wens',padx=5,pady=5)
make_operation_button('*').grid(row=4,column=3, stick='wens',padx=5,pady=5)
make_calc_button('=').grid(row=4,column=2, stick='wens',padx=5,pady=5)
make_clear_button('C').grid(row=4,column=1, stick='wens',padx=5,pady=5)

win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)

win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)





win.mainloop()


