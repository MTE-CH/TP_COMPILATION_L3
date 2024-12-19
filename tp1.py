from tkinter import *
root = Tk()
root.geometry('600x400')
root.title('Home')
def ansower():
    name = text.get('1.0','end')

    label['text'] = name

button = Button(text='أضغط هنا',bg='black',fg='white',command=ansower)
button.place(x =260, y =240)

labelTitle = Label(root,text='First TP compalition',bg='blue')
labelTitle.place(x=0,y=0)

text = Text(root,bg='gray',height=10,width=22)
text.place(x=40,y=45)

label = Label(root,bg='gray',height=10,width=24,anchor='nw')
label.place(x=380,y=45)

root.mainloop()