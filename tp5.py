
import tkinter as tk
from tkinter import filedialog, ttk

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.geometry('900x600')
root.title("TP3 Compilation")
root.config(bg='#f0f0f0')

# الخطوط والألوان
FONT_TITLE = ("Arial", 14, "bold")
FONT_TEXT = ("Arial", 12)
BG_COLOR = "#ffffff"
BTN_COLOR = "#4CAF50"
BTN_TEXT_COLOR = "#ffffff"

# منطقة النص للإدخال
textPlace = tk.Text(root, bg=BG_COLOR, font=FONT_TEXT, wrap=tk.WORD)
textPlace.place(x=50, y=100, width=400, height=300)

# إضافة شريط تمرير لمنطقة النص
scrollbar = tk.Scrollbar(root, command=textPlace.yview)
textPlace.config(yscrollcommand=scrollbar.set)
scrollbar.place(x=450, y=100, height=300)

# منطقة النص للإخراج
outputFrame = tk.LabelFrame(root, text="Output", font=FONT_TITLE, bg=BG_COLOR, fg="black")
outputFrame.place(x=500, y=100, width=350, height=300)

outputLabel = tk.Text(outputFrame, bg=BG_COLOR, font=FONT_TEXT, state='disabled', wrap=tk.WORD)
outputLabel.place(x=10, y=10, width=320, height=260)

outputScrollbar = tk.Scrollbar(outputFrame, command=outputLabel.yview)
outputLabel.config(yscrollcommand=outputScrollbar.set)
outputScrollbar.place(x=330, y=10, height=260)


# دالة معالجة النص
def process_sentence(sentence):
    def validate_word(word):
        if len(word) > 0 and not (('0' <= word[0] <= '9') or word[0] == '-' or word[0] == '+'):
            return "Erreur"
        for char in word[1:]:
            if not ('0' <= char <= '9'):
                return "Erreur"
        if '+' in word[1:] or '-' in word[1:]:
            return "Erreur"
        long = len(word) - 1 if word[0] in "+-" else len(word)
        if long >= 8:
            return "Erreur"

        if int(word) > 1657634:
            return "Erreur"
        return word

    result_string = ""
    word = ""
    in_word = False

    for char in sentence:
        if char == ' ' or char == '\n':
            if in_word:
                if word:
                    validated_word = validate_word(word)
                    if result_string:
                        result_string += "#"
                    result_string += validated_word
                word = ""
                in_word = False
        else:
            word += char
            in_word = True

    if word:
        validated_word = validate_word(word)
        if result_string:
            result_string += "#"
        result_string += validated_word

    return result_string


# دوال القائمة
def openFile():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding="utf-8") as file:
            textPlace.delete("1.0", tk.END)
            textPlace.insert(tk.END, file.read())


def saveFile():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(textPlace.get("1.0", tk.END))


def clearText():
    textPlace.delete("1.0", tk.END)
    outputLabel.config(state='normal')
    outputLabel.delete("1.0", tk.END)
    outputLabel.config(state='disabled')


def exitApp():
    root.quit()


# دالة لعرض النص المعالج
def copyText():
    cleaned_text = process_sentence(textPlace.get('1.0', 'end'))
    outputLabel.config(state='normal')
    outputLabel.delete("1.0", tk.END)
    outputLabel.insert(tk.END, cleaned_text)
    outputLabel.config(state='disabled')


# زر نسخ النص
button = tk.Button(root, text="Process Text", command=copyText, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=FONT_TEXT)
button.place(x=380, y=450, width=150, height=40)

# شريط القوائم
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open", command=openFile)
file_menu.add_command(label="Save",

command = saveFile)
file_menu.add_command(label="Clear", command=clearText)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exitApp)

root.mainloop()
