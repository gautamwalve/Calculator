
from tkinter import * #This imports everything :: importing the libraries
expression=" "             #globally declared the expression variable
#function to update the expression in the text entry box
def press(num):
    global expression #point out the global expression variable
    expression=expression+str(num)#concatenation of string
    equation.set(expression) #update the expression by using set method
    
    #Function to evaluate the final expression
def equalpress():
        #Try and except block statement for handling errors wrt to zero division error etc
        try:
            global expression
            #Eval function evaluatuont he expression and str function converts the result into string
            total =str(eval(expression))
            equation.set(total)
            #initialise the expression variable by empty string
            expression = ""
            #if error is generated then handle by the except block
        except:
            equation.set("Error")
            expression=""
    
 #Function to clear the contents of text entry box
def clear():
    global expression
    expression=""
    equation.set("")


#DriverCode

#Create a GUI WIndow
gui=Tk()

#Set Window Background
gui.configure(background="black")
#set configuration of Window
gui.geometry('270x150')
#Set GUI Title
gui.title("Simple Calculator")
#Creating Expression field
equation=StringVar()
expression_field=Entry(gui,textvariable=equation)
expression_field.grid(columnspan=4,ipadx=70)
#Creating Buttons
button1=Button(gui,text='1',fg='white',bg='black',command=lambda:press(1),height=1,width=5)
button1.grid(row=2,column=0)
button2=Button(gui,text='2',fg='white',bg='black',command=lambda:press(2),height=1,width=5)
button2.grid(row=2,column=1)
button3=Button(gui,text='3',fg='white',bg='black',command=lambda:press(3),height=1,width=5)
button3.grid(row=2,column=2)
button4=Button(gui,text='4',fg='white',bg='black',command=lambda:press(4),height=1,width=5)
button4.grid(row=3,column=0)
button5=Button(gui,text='5',fg='white',bg='black',command=lambda:press(5),height=1,width=5)
button5.grid(row=3,column=1)
button6=Button(gui,text='6',fg='white',bg='black',command=lambda:press(6),height=1,width=5)
button6.grid(row=3,column=2)
button7=Button(gui,text='7',fg='white',bg='black',command=lambda:press(7),height=1,width=5)
button7.grid(row=4,column=0)
button8=Button(gui,text='8',fg='white',bg='black',command=lambda:press(8),height=1,width=5)
button8.grid(row=4,column=1)
button9=Button(gui,text='9',fg='white',bg='black',command=lambda:press(9),height=1,width=5)
button9.grid(row=4,column=2)
button10=Button(gui,text='0',fg='white',bg='black',command=lambda:press(0),height=1,width=5)
button10.grid(row=5,column=0)
plus=Button(gui,text='+',fg='white',bg='black',command=lambda:press('+'),height=1,width=5)
plus.grid(row=2,column=3)
multiply=Button(gui,text='*',fg='white',bg='black',command=lambda:press('*'),height=1,width=5)
multiply.grid(row=3,column=3)
divide=Button(gui,text='/',fg='white',bg='black',command=lambda:press('/'),height=1,width=5)
divide.grid(row=4,column=3)
minus=Button(gui,text='-',fg='white',bg='black',command=lambda:press('-'),height=1,width=5)
minus.grid(row=5,column=1)
decimal=Button(gui,text='.',fg='white',bg='black',command=lambda:press('.'),height=1,width=5)
decimal.grid(row=5,column=2)
equal=Button(gui,text='=',fg='white',bg='black',command=equalpress,height=1,width=5)
equal.grid(row=5,column=3)
clear=Button(gui,text='clear',fg='white',bg='black',command=clear,height=1,width=5)
clear.grid(row=6,column=0)



#main Loop
gui.mainloop()

