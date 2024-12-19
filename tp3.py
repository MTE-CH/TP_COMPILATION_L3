import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.geometry('600x400')
root.title("TP2 COMPALATION")

textPlace = tk.Text(root, bg='gray', height=10, width=22)
textPlace.place(x=40, y=45)

label = tk.Label(root, bg='gray', height=10, width=24, anchor='nw')
label.place(x=380, y=45)

def cleanYourCode(text):
    insideDollar = False
    temp = ''
    result = ''
    for char in text:
        if char == '$':
            if insideDollar:
                insideDollar = False
                temp = ''
            else:
                insideDollar = True
        elif insideDollar:
            temp += char
        else:
            if char != ' ' and char != '\n':
                result += char
    if insideDollar:
        result += temp
    return result

def copyText():
    cleaned_text = cleanYourCode(textPlace.get('1.0', 'end'))
    label['text'] = cleaned_text

button = tk.Button(root, text="Copy Text", command=copyText)
button.place(x=260, y=240)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

def openFile():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding="utf-8") as file:
            textPlace.delete("1.0", tk.END)
            textPlace.insert(tk.END, file.read())

file_menu.add_command(label="Open", command=openFile)

def saveFile():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(textPlace.get("1.0", tk.END))

file_menu.add_command(label="Save", command=saveFile)

def clearText():
    textPlace.delete("1.0", tk.END)
    label['text'] = ''

file_menu.add_command(label="Remove", command=clearText)

def exitApp():
    root.quit()

file_menu.add_command(label="Exit", command=exitApp)

root.mainloop()