from tkinter import *
import math

# ex = ''
def click(value):
    ex = entrybox.get()
    ans = ''

    if value == 'del':
        ex =ex[:-1]
        entrybox.delete(0,END)
        entrybox.insert(0,ex)


    elif value =='C':
        entrybox.delete(0, END)


    elif value == '√':
        ans = math.sqrt(eval(ex))

    elif value == 'π':
        ans = math.pi

    elif value == '2π':
        ans = 2*math.pi

    elif value == 'cosx':
        ans = math.cos(math.radians(eval(ex)))

    elif value == 'cosh':
        ans = math.cosh(math.radians(eval(ex)))


    elif value == 'sinx':
        ans = math.sin(math.radians(eval(ex)))

    elif value == 'tanx':
        ans = math.tan(math.radians(eval(ex)))

    elif value == 'sinh':
        ans = math.sinh(math.radians(eval(ex)))

    elif value == 'tanh':
        ans = math.tanh(math.radians(eval(ex)))

    elif value == chr(8731):
        ans = eval(ex)**(1/3)

    elif value == "x\u02b8":
        entrybox.insert(END,'**')

    elif value == "x\u00b3":
        ans = eval(ex)**(3)

    elif value == "x\u00b2":
        ans = eval(ex)**(2)

    elif value == "ln":
        ans = math.log((eval(ex)))
    elif value == "log2":
        ans = math.log2((eval(ex)))
    elif value == "deg":
        ans = math.degrees((eval(ex)))
    elif value == "rad":
        ans = math.radians((eval(ex)))

    elif value == "e":
        ans = math.e

    elif value == "log10":
        ans = math.log10((eval(ex)))

    elif value == "x!":
        ans = math.factorial((eval(ex)))

    elif value == chr(247):
        entrybox.insert(END,'/')
        return

    elif value == "=":
        ans =eval(ex)

    else:
        entrybox.insert(END,value)
        return

    entrybox.delete(0, END)
    entrybox.insert(0, ans)



root = Tk()
root.geometry("345x655+100+100")
root.config(bg='teal')
root.title("Scientific Calculator")
root.resizable(0,0)

# Creating entry box
entrybox = Entry(root, font=('arial', 20, 'bold'), bg="white", fg="black", bd=10)
entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky='nsew')

# Creating buttons
button_text_list = ['C','e','deg','rad',
                    'x!',"x\u00b3","x\u00b2","x\u02b8"
                    ,chr(8731),'cosx','tanx','sinx',
                    '√','cosh', 'tanh', 'sinh',
                     '(",")','ln','log2','log10'
                    ,'2π','π','%',chr(247),
                    '7','8', '9', '*',
                    '4','5','6','-',
                    '1','2','3','+',
                    '0','.','=', 'del']

rowvalue = 1
columnvalue = 0

for i in button_text_list:
    button = Button(root, text=i, fg="teal", width=2, height=2, bd=2, bg='white', relief=RAISED, font=('arial', 12, 'bold'),
                    activebackground='teal', justify=RIGHT,command = lambda button = i:click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=2, padx=2, sticky='nsew')
    columnvalue += 1
    if columnvalue > 3:
        rowvalue += 1
        columnvalue = 0

root.mainloop()
