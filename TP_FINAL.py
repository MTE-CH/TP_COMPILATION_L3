class FSM:
    # Definiton of FSM elements
    error_type = "NO ERROR"
    keyWord = ["PROGRAM", "BEGIN", "END.", "CONST", "INT", "REAL", "BOOLEAN", "FOR", "WHILE", "IF", "ELSE", "CONTINUE",
               "BREACK", "DO", "ELIF"]
    states = ["start0", "Processing1", "Processing2", "Processing3", "Relational_Operator1", "Relational_Operator2",
              "Boolean_Operator1", "Boolean_Operator2", "Assignment_Operator0", "Separator0", "Integer0", "Float0",
              "Identificator0", "Arithmetic_Operator1", "Arithmetic_Operator2", "Arithmetic_Operator3"]
    final_states = ["Relational_Operator1", "Relational_Operator2", "Boolean_Operator1", "Boolean_Operator2",
                    "Assignment_Operator0", "Separator0", "Integer0", "Float0", "Identificator0",
                    "Arithmetic_Operator1", "Arithmetic_Operator2", "Arithmetic_Operator3"]
    initial_state = "start0"
    events = ["=", "<", ">", "!", "&", "|", "*", "/", "-", "+", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".",
              "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z", ";", ",", "[", "]", ":", "(", ")", "}", "{", "_"]
    transition_table = [
        #    =                            <                           >                            !                       &                        |                        *                           /                           -                           +                           0                   1                  2                   3                   4                   5                   6                   7                   8                    9                  .              a                     b                     c                     d                     e                     f                     g                     h                     i                     j                     k                     l                     m                     n                     o                     p                     q                     r                     s                     t                     u                     v                     w                     x                     y                     z                     ;                 ,                 [                 ]                 :                 (                 )                 }                 {                 _
        ["Assignment_Operator0", "Relational_Operator1", "Relational_Operator1", "Boolean_Operator1",
         "Boolean_Operator2", "Boolean_Operator2", "Arithmetic_Operator1", "Arithmetic_Operator1",
         "Arithmetic_Operator2", "Arithmetic_Operator3", "Integer0", "Integer0", "Integer0", "Integer0", "Integer0",
         "Integer0", "Integer0", "Integer0", "Integer0", "Integer0", None, "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0",
         "Separator0", "Separator0", "Separator0", "Separator0", "Separator0", "Separator0", "Separator0", "Separator0",
         "Separator0", None],  # start0
        [None, None, None, None, None, None, None, None, None, None, "Float0", "Float0", "Float0", "Float0", "Float0",
         "Float0", "Float0", "Float0", "Float0", "Float0", None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None],  # Processing1
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, "Processing3"],  # Processing2
        [None, None, None, None, None, None, None, None, None, None, "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", None, "Identificator0", "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0", None, None, None,
         None, None, None, None, None, None, "Processing2"],  # Processing3
        ["Relational_Operator2", None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None],  # Relational_Operator1
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None],  # Relational_Operator2
        ["Relational_Operator2", None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None],  # Boolean_Operator1
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None],  # Boolean_Operator2
        ["Relational_Operator2", None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None],  # Assignment_Operator0
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None],  # Separator0
        [None, None, None, None, None, None, None, None, None, None, "Integer0", "Integer0", "Integer0", "Integer0",
         "Integer0", "Integer0", "Integer0", "Integer0", "Integer0", "Integer0", "Processing1", None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None],  # Integer0
        [None, None, None, None, None, None, None, None, None, None, "Float0", "Float0", "Float0", "Float0", "Float0",
         "Float0", "Float0", "Float0", "Float0", "Float0", None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None],  # Float0
        [None, None, None, None, None, None, None, None, None, None, "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", None, "Identificator0", "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0",
         "Identificator0", "Identificator0", "Identificator0", "Identificator0", "Identificator0", None, None, None,
         None, None, None, None, None, None, "Processing3"],  # Identificator0
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None],  # Arithmetic_Operator1
        [None, None, None, None, None, None, None, None, "Arithmetic_Operator1", None, "Integer0", "Integer0",
         "Integer0", "Integer0", "Integer0", "Integer0", "Integer0", "Integer0", "Integer0", "Integer0", None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        # Arithmetic_Operator2
        [None, None, None, None, None, None, None, None, None, "Arithmetic_Operator1", "Integer0", "Integer0",
         "Integer0", "Integer0", "Integer0", "Integer0", "Integer0", "Integer0", "Integer0", "Integer0", None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        # Arithmetic_Operator3
    ]

    def read(self, word):
        self.error_type = "NO ERROR"
        current_state = "start0"
        if word in self.keyWord: return "keyword"

        for letter in word:
            if letter not in self.events:
                self.error_type = "[ " + letter + " ]" + " is not in the FSM alphabet"
                return "ERROR"
            current_index = self.states.index(current_state)
            event_index = self.events.index(letter)
            new_state = self.transition_table[current_index][event_index]
            if new_state is None:
                self.error_type = "the FSM has been blocked"
                return "ERROR"
            current_state = new_state

        if current_state in self.final_states:
            if current_state == "Float0":
                if len(word) > 9:
                    self.error_type = "the lenght of the flaot number is maore than 9 chars"
                    return "ERROR"
            if current_state == "Integer0":
                if len(word) > 7:
                    self.error_type = "the lenght of the integer number is more than 7 chars"
                    return "ERROR"
                if int(word) > 1657634:
                    self.error_type = "the value of the integer number is more than 1657634"
                    return "ERROR"
            if current_state == "Identificator0":
                if len(word) > 40:
                    self.error_type = "the lenght of the indentificator is more than 40 chars"
                    return "ERROR"
            return current_state[:-1]


    def reset_errors(self):
        self.error_type = "NO ERROR"


from tkinter import *
from tkinter import filedialog


# def check_structure(code):
#     errors = ""
#
#     # التحقق من البداية بـ PROGRAM
#     first_line = ""
#     for char in code:
#         if char == '\n':
#             break
#         first_line += char
#
#     if len(first_line) >= 8 and first_line[:7] == "PROGRAM" and first_line[-1] == ";":
#         program_name = first_line[8:-1]
#         if not program_name:
#             errors += "اسم البرنامج مفقود بعد 'PROGRAM '.\n"
#         else:
#             for char in program_name:
#                 if not ('a' <= char <= 'z'):  # اسم البرنامج يجب أن يحتوي فقط على حروف صغيرة
#                     errors += "اسم البرنامج يجب أن يكون بحروف صغيرة فقط وبدون أرقام أو رموز.\n"
#                     break
#     else:
#         errors += "السطر الأول يجب أن يكون من الشكل: PROGRAM nom_program;\n"
#
#     # التحقق من وجود BEGIN و END.
#     has_begin = False
#     has_end = False
#
#     for i in range(len(code) - 4):
#         if code[i:i + 5] == "BEGIN":
#             has_begin = True
#         if code[i:i + 4] == "END.":
#             has_end = True
#             # التحقق من وجود كلمات بعد END.
#             after_end = code[i + 4:].strip()
#             if after_end:
#                 errors += "لا يجب أن يكون هناك كلمات وراء END.\n"
#
#     if not has_begin:
#         errors += "الكود يجب أن يحتوي على الكلمة المفتاحية 'BEGIN'.\n"
#         return [error for error in errors.split("\n") if error] if errors else []
#     if not has_end:
#         errors += "الكود يجب أن يحتوي على الكلمة المفتاحية 'END.'.\n"
#         return [error for error in errors.split("\n") if error] if errors else []
#
#     # التحقق من جزء الديكلاراسيون
#     if has_begin:
#         begin_index = -1
#         for i in range(len(code) - 4):
#             if code[i:i + 5] == "BEGIN":
#                 begin_index = i
#                 break
#
#         declaration_part = ""
#         for i in range(begin_index):
#             declaration_part += code[i]
#
#         lines = []
#         line = ""
#         for char in declaration_part:
#             if char == '\n':
#                 if line:
#                     lines += [line]
#                 line = ""
#             else:
#                 line += char
#         if line:
#             lines += [line]
#
#         for current_line in lines:
#             if ":" in current_line and ";" in current_line:
#                 valid_declaration = False
#                 for dtype in ["INT", "REAL", "BOOLEAN", "CHAR", "STRING"]:
#                     if dtype in current_line:
#                         valid_declaration = True
#                         break
#                 if not valid_declaration:
#                     errors += "جزء الإعلان غير صحيح أو مفقود.\n"
#                     break
#
#     # التحقق من الأوامر في قسم التعليمات
#     if has_begin and has_end:
#         begin_index = -1
#         end_index = -1
#
#     for i in range(len(code) - 4):
#         if code[i:i + 5] == "BEGIN" and begin_index == -1:
#             begin_index = i + 5
#         if code[i:i + 4] == "END." and end_index == -1:
#             end_index = i
#
#     # استخراج النص بين BEGIN و END.
#     instructions = ""
#     for i in range(begin_index, end_index):
#         instructions += code[i]
#
#     if not instructions.strip():
#         errors += "قسم التعليمات بين BEGIN و END. لا يمكن أن يكون فارغًا.\n"
#
#
#
#     return [error for error in errors.split("\n") if error] if errors else []
def check_structure(code):
    errors = ""

    # التحقق من البداية بـ PROGRAM
    first_line = ""
    for char in code:
        if char == '\n':
            break
        first_line += char

    if len(first_line) >= 8 and first_line[:7] == "PROGRAM" and first_line[-1] == ";":
        program_name = first_line[8:-1]
        if not program_name:
            errors += "اسم البرنامج مفقود بعد 'PROGRAM '.\n"
        else:
            for char in program_name:
                if not ('a' <= char <= 'z'):  # اسم البرنامج يجب أن يحتوي فقط على حروف صغيرة
                    errors += "اسم البرنامج يجب أن يكون بحروف صغيرة فقط وبدون أرقام أو رموز.\n"
                    break
    else:
        errors += "السطر الأول يجب أن يكون من الشكل: PROGRAM nom_program;\n"

    # التحقق من وجود BEGIN و END.
    has_begin = False
    has_end = False

    for i in range(len(code) - 4):
        if code[i:i + 5] == "BEGIN":
            has_begin = True
        if code[i:i + 4] == "END.":
            has_end = True
            # التحقق من وجود كلمات بعد END.
            after_end = code[i + 4:].strip()
            if after_end:
                errors += "لا يجب أن يكون هناك كلمات وراء END.\n"

    if not has_begin:
        errors += "الكود يجب أن يحتوي على الكلمة المفتاحية 'BEGIN'.\n"
        return [error for error in errors.split("\n") if error] if errors else []
    if not has_end:
        errors += "الكود يجب أن يحتوي على الكلمة المفتاحية 'END.'.\n"
        return [error for error in errors.split("\n") if error] if errors else []

    # التحقق من جزء الإعلان
    if has_begin:
        begin_index = -1
        for i in range(len(code) - 4):
            if code[i:i + 5] == "BEGIN":
                begin_index = i
                break

        declaration_part = ""
        for i in range(begin_index):
            declaration_part += code[i]

        lines = []
        line = ""
        for char in declaration_part:
            if char == '\n':
                if line:
                    lines += [line.strip()]
                line = ""
            else:
                line += char
        if line:
            lines += [line.strip()]

        for current_line in lines:
            if current_line and not current_line.endswith(';'):
                errors += "كل الأسطر في جزء الإعلان يجب أن تنتهي بـ ;\n"
                break

    # التحقق من الأوامر في قسم التعليمات
    if has_begin and has_end:
        begin_index = -1
        end_index = -1

        for i in range(len(code) - 4):
            if code[i:i + 5] == "BEGIN" and begin_index == -1:
                begin_index = i + 5
            if code[i:i + 4] == "END." and end_index == -1:
                end_index = i

        # استخراج النص بين BEGIN و END.
        instructions = ""
        for i in range(begin_index, end_index):
            instructions += code[i]

        if not instructions.strip():
            errors += "قسم التعليمات بين BEGIN و END. لا يمكن أن يكون فارغًا.\n"

        # التحقق من انتهاء كل الأسطر في التعليمات بـ ;
        instruction_lines = []
        line = ""
        for char in instructions:
            if char == '\n':
                if line:
                    instruction_lines += [line.strip()]
                line = ""
            else:
                line += char
        if line:
            instruction_lines += [line.strip()]

        for current_line in instruction_lines:
            if current_line and not current_line.endswith(';'):
                errors += "كل الأسطر في قسم التعليمات يجب أن تنتهي بـ ;\n"
                break

    return [error for error in errors.split("\n") if error] if errors else []


def methode_lecture(code):
    code = cleanYourCode(code)
    code0 = ""
    length = len(code) - 1
    i = 0

    while i <= length:  # تعديل الشرط هنا ليكون <= بدلاً من <
        if i + 1 <= length and code[i] == '+' and code[i + 1] == '+':
            code0 += ' ++ '
            i += 2
            continue

        if i + 1 <= length and code[i] == '=' and code[i + 1] == '=':
            code0 += ' == '
            i += 2
            continue
        if i + 1 <= length and code[i] == '!' and code[i + 1] == '=':
            code0 += ' != '
            i += 2
            continue
        if i + 1 <= length and code[i] == '<' and code[i + 1] == '=':
            code0 += ' <= '
            i += 2
            continue
        if i + 1 <= length and code[i] == '>' and code[i + 1] == '=':
            code0 += ' >= '
            i += 2
            continue
        if i + 3 <= length and code[i:i + 4] == "END.":
            code0 += "END."
            i += 4
            continue
        if i + 1 <= length and code[i] == '-' and code[i + 1] == '-':
            code0 += ' -- '
            i += 2
            continue

        if code[i] in ['+', '-', '*', '/', '(', ')', '[', ']', '{', '}', '=', ',', ';']:
            if i + 1 <= length and code[i] in ['+', '-'] and code[i + 1] == code[i] and ('a' <= code[i - 1] <= 'z'):
                code0 += ' ' + code[i] + code[i + 1] + ' '  # i++ --> i ++
                i += 2
            else:
                code0 += ' ' + code[i] + ' '
                i += 1
            continue

        if code[i] != ' ' and code[i] != '\n':
            code0 += code[i]
            i += 1
        else:
            code0 += ' '
            i += 1
            while i <= length and (code[i] == ' ' or code[i] == '\n'):
                i += 1

    return code0


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import re

def cleanYourCode(text):
    # التعبير المنتظم للبحث عن النصوص المحاطة بعلامتي $
    # لا يتم التعامل مع النصوص إذا كانت تحتوي على أكثر من $ متداخلة
    pattern = r'\$(.*?)\$'
    # إزالة النصوص التي تطابق النمط
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text




# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def methode_write(processed_code):
    fsm = FSM()
    result = ""
    word = ""
    index = 1
    for char in processed_code:

        if char == ' ':
            if word:
                # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                result += fsm.read(word) + ": " + word + "\n"  # str باش يلصق حرف مع رقم عادي
                index += 1
                word = ""
        else:  # الحالة الاولى راح يبدى من هنا
            word += char

    if word:
        result += fsm.read(word) + ": " + word + "\n"

    return result


def analyze_code():
    """
    تحليل النص المدخل وعرض النتائج في واجهة المستخدم.
    """
    input_code = text.get('1.0', END)
    processed_code = methode_lecture(input_code)
    # label.config(text=processed_code)
    analyzed_code1 = methode_write(processed_code)
    # label1.config(text=analyzed_code1)

    # التحقق من الهيكل
    structure_errors = check_structure(input_code)
    if structure_errors:
        error_message = "\n".join(structure_errors)
        # label2.config(text=error_message)
        label3.config(text=error_message)

    else:

        processed_code = methode_lecture(input_code)
        # label.config(text=processed_code)

        analyzed_code = methode_lecture(processed_code)
        # label2.config(text=analyzed_code)

        analyzed2_code = methode_write(analyzed_code)
        label3.config(text=analyzed2_code)


def len(text):
    length = 0

    for i in text:
        length += 1

    return length


root = Tk()
root.geometry('1200x1200')
root.title('Code Analyzer')

menubar = Menu(root)
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file_menu)


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
        text.delete("1.0", END)
        text.insert("1.0", content)


def save_file():
    content = text.get("1.0", END).strip()
    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if save_path:
        with open(save_path, 'w') as file:
            file.write(content)

def clearText():
    text.delete("1.0", END)
    Label['text'] = ''

file_menu.add_command(label="Remove", command=clearText)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)
root.config(menu=menubar)

label4_title = Label(root, text="input", bg='lightgray', font=("Arial", 12, "bold"))
label4_title.place(x=150, y=55)

text = Text(root, bg='lightgray', height=30, width=45)
text.place(x=150, y=80)

button = Button(root, text='Analyze Code', bg='black', fg='white', command=analyze_code, width=15, height=2)
button.place(x=540, y=250)

# label = Label(root, bg='lightgray', height=20, width=50, anchor='nw')
# label.place(x=800, y=45)


# label1 = Label(root, bg='lightgray', height=20, width=50, anchor='nw')
# label1.place(x=800, y=400)

# label2 = Label(root, bg='lightgray', height=15, width=50, anchor='nw', justify='left')
# label2.place(x=650, y=450)

label3_title = Label(root, text="Terminal", bg='lightgray', font=("Arial", 12, "bold"))
label3_title.place(x=750, y=55)

label3 = Label(root, bg='lightgray', height=20, width=90, anchor='nw', justify='left')
label3.place(x=750, y=80)
# تشغيل التطبيق
root.mainloop()