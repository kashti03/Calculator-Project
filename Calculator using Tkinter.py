from tkinter import *
import ast             #Abstract Syntax Tree

i=0
def getnumber(number):
    global i
    input.insert(i,number)  #i is the index position which defines where on the display screen you want to add the number
    i+=1

def getoperator(operator):
    global i
    length = len(operator)
    input.insert(i,operator)
    i+=length

def delete():
    input.delete(0,END) #deletes all the entries

def calculate():
    entire_string = input.get()
    try:
        node = ast.parse(entire_string,mode="eval")                          #saving parsed expression in node
        result = eval(compile(node,'<string>','eval'))
        delete()                                                             #to all clear the entered digits and only display result
        input.insert(0,result)

    except Exception:
        delete()
        input.insert(0,"Error")

def undo():
    string = input.get()
    if len(string):            #if length of string is not zero
        new = string[:-1]      # string except for the last input
        delete()
        input.insert(0,new)

root = Tk()

input = Entry(root)
input.grid(row=0,columnspan=15)

numbers = ["1","2","3","4","5","6","7","8","9"]
count = 0

for x in range(3):
    for y in range(3):
        button_text = numbers[count]
        button=Button(root,text=button_text,width=3,command= lambda text=button_text:getnumber(text))
        button.grid(row=x+1,column=y)
        count+=1

zero = Button(root,text="0",width=3,command = lambda :getnumber(0))
zero.grid(row=4,column=1)

operations=["+","-","/","*","**","*3.14","(",")","%","**2"]

counter = 0
for x in range(4):
    for y in range(3):
        if counter < len(operations):
            op_buttons = Button(root,text=operations[counter],width=3,command= lambda text=operations[counter]:getoperator(text))
            op_buttons.grid(row=x+1,column=y+3)
            counter+=1

all_clear = Button(root,text="AC",width=3,command=delete)
all_clear.grid(row=4,column=0)

equals = Button(root,text="=",width=3,command=calculate)
equals.grid(row=4,column=2)

backspace = Button(root,text="<-",width=3,command=undo)
backspace.grid(row=4,column=4)

root.mainloop()
