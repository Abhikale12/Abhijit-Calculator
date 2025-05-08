import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Abhijit Calculator")
root.resizable(False, False)

expression = ""

themes = {
    "light": {
        "bg": "#F2F2F2",
        "fg": "#000000",
        "entry_bg": "#FFFFFF",
        "entry_fg": "#000000",
        "button_bg": "#E0E0E0",
        "operator_bg": "#FFA500",
        "equal_bg": "#32CD32",
        "clear_bg": "#FF6347",
        "back_bg": "#4682B4",
        "toggle_bg": "#D3D3D3"
    },
    "dark": {
        "bg": "#2E2E2E",
        "fg": "#FFFFFF",
        "entry_bg": "#1C1C1C",
        "entry_fg": "#F2F2F2",
        "button_bg": "#4B4B4B",
        "operator_bg": "#FF9500",
        "equal_bg": "#34C759",
        "clear_bg": "#FF3B30",
        "back_bg": "#1E90FF",
        "toggle_bg": "#A9A9A9"
    }
}

current_theme = "dark"

def apply_theme():
    theme = themes[current_theme]
    root.configure(bg=theme["bg"])
    expression_field.configure(bg=theme["entry_bg"], fg=theme["entry_fg"])
    for btn in buttons_list:
        btn_text = btn["text"]
        if btn_text in ['+', '-', '*', '/']:
            btn.configure(bg=theme["operator_bg"], fg=theme["fg"])
        elif btn_text == '=':
            btn.configure(bg=theme["equal_bg"], fg=theme["fg"])
        elif btn_text == 'C':
            btn.configure(bg=theme["clear_bg"], fg=theme["fg"])
        elif btn_text == '←':
            btn.configure(bg=theme["back_bg"], fg=theme["fg"])
        elif btn_text == 'Day/Night':
            btn.configure(bg=theme["toggle_bg"], fg=theme["fg"])
        elif btn_text == '%':
            btn.configure(bg=theme["operator_bg"], fg=theme["fg"])
        else:
            btn.configure(bg=theme["button_bg"], fg=theme["fg"])

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress(event=None):
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

def clear(event=None):
    global expression
    expression = ""
    equation.set("")

def backspace(event=None):
    global expression
    expression = expression[:-1]
    equation.set(expression)

def percentage(event=None):
    global expression
    try:
        if expression:
            result = str(eval(expression + "/100"))
            equation.set(result)
            expression = result
    except:
        equation.set("Error")
        expression = ""

def toggle_theme():
    global current_theme
    current_theme = "light" if current_theme == "dark" else "dark"
    apply_theme()

def key_handler(event):
    key = event.char
    if key in '0123456789.+-*/':
        press(key)
    elif key == '%':
        percentage()
    elif key == '\r':  # Enter
        equalpress()
    elif key == '\x08':  # Backspace
        backspace()
    elif key == '\x1b':  # Escape
        clear()

equation = tk.StringVar()

expression_field = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2,
                            width=25, borderwidth=4, justify='right')
expression_field.grid(row=0, column=0, columnspan=4)

buttons = [
    ('C', 1, 0), ('←', 1, 1), ('Day/Night', 1, 2), ('%', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
]

buttons_list = []

for (text, row, col) in buttons:
    if text == '=':
        action = equalpress
    elif text == 'C':
        action = clear
    elif text == '←':
        action = backspace
    elif text == 'Day/Night':
        action = toggle_theme
    elif text == '%':
        action = percentage
    else:
        action = lambda x=text: press(x)
    btn = tk.Button(root, text=text, padx=20, pady=20, bd=0,
                    font=('Arial', 18), command=action)
    btn.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)
    buttons_list.append(btn)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

apply_theme()

# Bind keys
root.bind("<Key>", key_handler)
root.bind("<Return>", equalpress)
root.bind("<BackSpace>", backspace)
root.bind("<Escape>", clear)

# Run app
root.mainloop()
