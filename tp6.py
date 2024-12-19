from tkinter import filedialog

from tkinter import *


app = Tk()


app.title("TP Compilation")


inputLabel = Text(app, width=40, height=25)


inputLabel.grid(row=3, column=1, padx=20, pady=10, ipady=10)


outputLabel = Label(app, width=40, height=25, bg="white",

                    relief="solid", anchor="nw", justify=LEFT, wraplength=290)


outputLabel.grid(row=3, column=2, padx=20, pady=10, ipady=10)


def length(text):

    length = 0

    for i in text:

        length += 1

    return length


def removeNewLine(text):

    text = list(text)

    for i in range(length(text)):

        if text[i] == '\n':

            text[i] = " "

    text = "".join(text)

    return text


def getNumbers(text):

    numbers = []

    number = ""

    for char in text:

        if char != " ":

            number += char

        elif number:

            numbers.append(number)

            number = ""

    if number:

        numbers.append(number)

    return numbers


def isNumber(character): return '0' <= character <= '9'


def isSign(character): return character == '+' or character == '-'


def isPoint(character): return character == '.'


def calcPoint(number):

    point = 0

    for i in range(length(number)):

        if number[i] == '.':

            point += 1

    return point


def isFloat(number):

    if isSign(number[0]) and length(number) == 1:
        return False

    if isSign(number[0]) and not isNumber(number[1]):
        return False

    if isSign(number[0]) or isNumber(number[0]):

        for i in range(1, length(number)):
            if not (isNumber(number[i]) or isPoint(number[i])):
                return False

        if calcPoint(number) > 1:
            return False

        if number[length(number)-1] == '.':
            return False

        return True

    return False


def numberNotLonger(number):
    return length(number) <= 9


def verifieNumber(number):
    return isFloat(number) and numberNotLonger(number)


def verifieNumbers():

    text = inputLabel.get("1.0", END)

    text = removeNewLine(text)

    textNumbers = getNumbers(text)

    text = ""

    for i, number in enumerate(textNumbers):
        if verifieNumber(number):
            text += number
        else:
            text += "Error"

        if i < length(textNumbers) - 1:
            text += "#"

    outputLabel.config(text=text)


verfieNumberButton = Button(

    app, text="Verifie Numbers", command=verifieNumbers)


verfieNumberButton.grid(row=4, column=1, columnspan=2, padx=20, pady=10)


menuBar = Menu(app)


app.config(menu=menuBar)


fileMenu = Menu(menuBar, tearoff=0)


menuBar.add_cascade(label="File", menu=fileMenu)


def openFile():

    filePath = filedialog.askopenfilename(title="Open File", filetypes=(

        ("Text Files", "*.txt"), ("All Files", "*.*")))

    if filePath:

        with open(filePath, "r") as file:

            inputLabel.delete("1.0", END)

            inputLabel.insert(END, file.read())


fileMenu.add_command(label="Open", command=openFile)


def saveFile():

    filePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(

        ("Text Files", "*.txt"), ("All Files", "*.*")))

    if filePath:

        with open(filePath, "w") as file:

            file.write(inputLabel.get("1.0", END))


fileMenu.add_command(label="Save", command=saveFile)


def removeText():

    inputLabel.delete("1.0", END)

    outputLabel.config(text="")


fileMenu.add_command(label="Remove", command=removeText)


fileMenu.add_command(label="Exit", command=app.quit)


app.mainloop()
