from tkinter import * 
from tkinter import filedialog 
 
 
def open_file():  
    chose_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])  # فتح مربع حوار لاختيار ملف نصي فقط 
    if chose_file:   
        file= open(chose_file, 'r')   # فتح الملف للقراءة 
        text = file.read()  # قراءة المحتوى 
        text.delete("1.0", END)  # مسح النص القديم من text 
        text.insert("1.0", text)  # إدراج النص الجديد في text 
 
 
def save_file(): 
    content = text.get("1.0", END)                                                                                          # جلب النص من text 
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")]) 
    if save_path:                                                                                                           # التحقق من أن المستخدم قد اختار مسار الحفظ 
        with open(save_path, 'w') as file:  # فتح الملف في وضع الكتابة 
            file.write(content)  # حفظ النص في الملف 
 
def remove_text(): 
    text.delete("1.0", END)  # مسح محتوى text 
    label.config(text="")  # مسح محتوى label 
 
def isIdentificater(code0):
    if 'a' <= code0[0] <= 'z' and len(code0) <= 40 and code0[len(code0)-1] != '_' :
        i = 1
        lenght = len(code0)    
        while i < lenght:
            if  'a' <= code0[0] <= 'z' or '0' <= code0[0] <= '9':
                i += 1
                continue
            elif code0[i] == '_' :
                count = 0
                while code0[i] == '_':
                    count += 1
                    i += 1
                if count % 2 == 0 : return False
            else: return False
        return True   
    else: return False

def ansower(): 
    code = text.get('1.0', 'end')
    label.config(text = '')
    code0 = '' 
    lenght = len(code) - 1
    i = 0
    while i < lenght :
        if  code[i] == ' ' or code[i] == '\n':
            label.config(text = label.cget("text")+"#")
            i += 1
            while code[i] == ' ' or code[i] == '\n':
                i += 1
        else:
            while code[i] != ' ' and code[i] != '\n' :
                code0 += code[i]
                i += 1
            a = isIdentificater(code0)
            if a == True :
                label.config(text = label.cget("text")+code0)
                code0 = ''
            else:
                label.config(text = label.cget("text")+"error")

root = Tk() 
root.geometry('600x400') 
root.title('Home') 
 
menubar = Menu(root) 
file_menu = Menu(menubar, tearoff=0) 
menubar.add_cascade(label='File', menu=file_menu) 
file_menu.add_command(label='Open', command=open_file) 
file_menu.add_command(label='Save', command=save_file) 
file_menu.add_command(label='Remove', command=remove_text) 
file_menu.add_separator() 
file_menu.add_command(label='Exit', command=root.quit) 
root.config(menu=menubar) 
 
button = Button(root, text=' click', bg='black', fg='white', command=ansower) 
button.place(x=260, y=240) 
 
#labelTitle = Label(root, text='First TP Compilation', bg='blue', fg='white') 
#labelTitle.place(x=0, y=0) 
 
text = Text(root, bg='gray', height=10, width=22) 
text.place(x=40, y=45) 
 
 
label = Label(root, bg='gray', height=10, width=24, anchor='nw') 
label.place(x=380, y=45) 
 
# تشغيل التطبيق 
root.mainloop()