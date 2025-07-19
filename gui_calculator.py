import tkinter as tk
from functools import partial

# Basic calculator state
def calculate(expression):
    try:
        return str(eval(expression))
    except Exception:
        return "Error"

def main():
    root = tk.Tk()
    root.title("Python Calculator")

    expression = tk.StringVar()

    display = tk.Entry(root, textvariable=expression, font=("Helvetica", 24), bd=10, relief=tk.RIDGE, justify='right')
    display.grid(row=0, column=0, columnspan=4, sticky='nsew')

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]

    def on_button_click(char):
        if char == '=':
            result = calculate(expression.get())
            expression.set(result)
        else:
            expression.set(expression.get() + char)

    for (text, row, col) in buttons:
        action = partial(on_button_click, text)
        tk.Button(root, text=text, command=action, font=("Helvetica", 20), width=5, height=2).grid(row=row, column=col, sticky='nsew')

    # Clear button
    tk.Button(root, text='C', command=lambda: expression.set(''), font=("Helvetica", 20), width=5, height=2).grid(row=5, column=0, columnspan=4, sticky='nsew')

    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

if __name__ == '__main__':
    main()
