from tkinter import Tk
from tkinter import *
root=Tk()
root.title("Simple Calculator")
root.geometry('570x550')
root.resizable(False,False)
root.configure(bg='#000000')
equation=''
def clear():
    global equation
    equation=''
    label_result.config(text=equation)

def show(val):
    global equation
    equation+=val
    label_result.config(text=equation)

def calculate():
    global equation
    try:
        ans=eval(equation)  
    except:
        label_result.config(text="Error")
    try:
        label_result.config(text=ans)
    except:
        label_result.config(text="Error")


label_result=Label(root,width=40,height=2,text='',font=('arial',30))
Button(root,text='AC',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#FF0000',bg='#0000FF',command=lambda :clear()).place(x=5,y=80)
Button(root,text='/',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#2BEC2B',bg='#2BEC2B',command=lambda:show('/')).place(x=140,y=80)
Button(root,text='Mod(%)',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#330000',bg='#330000',command=lambda:show('%')).place(x=275,y=80)
Button(root,text='*',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#330000',bg='#330000',command=lambda:show('*')).place(x=410,y=80)

Button(root,text='+',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#330000',bg='#330000',command=lambda:show('+')).place(x=5,y=140)
Button(root,text='-',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#330000',bg='#330000',command=lambda:show('-')).place(x=140,y=140)
Button(root,text='9',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#330000',bg='#0000FF',command=lambda:show('9')).place(x=275,y=140)
Button(root,text='8',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#330000',bg='#330000',command=lambda:show('8')).place(x=410,y=140)
Button(root,text='7',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#330000',bg='#330000',command=lambda:show('7')).place(x=5,y=220)
Button(root,text='6',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#330000',bg='#330000',command=lambda:show('6')).place(x=140,y=220)

Button(root,text='5',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#330000',bg='#0000FF',command=lambda:show('5')).place(x=275,y=220)
Button(root,text='4',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#330000',bg='#330000',command=lambda:show('4')).place(x=410,y=220)
Button(root,text='3',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#330000',bg='#330000',command=lambda:show('3')).place(x=5,y=300)
Button(root,text='2',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#330000',bg='#330000',command=lambda:show('2')).place(x=140,y=300)


Button(root,text='1',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#330000',bg='#0000FF',command=lambda:show('1')).place(x=5,y=380)
Button(root,text='0',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#330000',bg='#330000',command=lambda:show('0')).place(x=140,y=380)
Button(root,text='.',width=5,height=1,font=('arial',30,'bold'),bd=1,fg='#330000',bg='#330000',command=lambda:show('.')).place(x=5,y=460)
Button(root,text='=',width=14,height=4,font=('arial',30,'bold'),bd=1,fg='#EC2B2B',bg='#EC2B2B',command=lambda:calculate()).place(x=275,y=300)
label_result.pack()
root.mainloop()