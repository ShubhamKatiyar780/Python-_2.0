import tkinter as tk
import math

root = tk.Tk()
root.geometry("320x500")
root.configure(bg="yellow")
root.resizable(True, True)
root.title("🧮 📱🖩 Calculator")

def update_display(charrr):
    current_text = display_var.get()
    display_var.set(current_text + str(charrr))

def calculate():
    try:
        result = eval(display_var.get().replace('√', 'math.sqrt').replace('%', '/100')
                      .replace('x\u00B3', '**3').replace('x²', '**2').replace('x', '*')
                      .replace('÷', '/').replace('—', '-').replace('•', '.'))
        display_var.set(result)
    except:
        display_var.set("Error")

def clear_last_entry():
    display_var.set(display_var.get()[:-1])

def clear_display():
    display_var.set("")

def square_root():
    try:
        value = float(display_var.get())
        display_var.set(math.sqrt(value))
    except:
        display_var.set("Error")

display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var,bg="pink",fg="blue", font=("Lucida Handwriting", 20), border=2, relief="ridge", justify="right")
display.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")


buttons = [
    ("%", 2, 0), ("√", 2, 1), ("C", 2, 2), ("⌫", 2, 3),
    ("(", 3, 0), (")", 3, 1), ("x²", 3, 2), ("÷", 3, 3),
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("x", 4, 3),
    ("4", 5, 0), ("5", 5, 1), ("6", 5, 2), ("—", 5, 3),
    ("1", 6, 0), ("2", 6, 1), ("3", 6, 2), ("+", 6, 3),
    ("x\u00B3", 7, 0), ("0", 7, 1), ("•", 7, 2), ("=", 7, 3)
]

for (text, row, col) in buttons:
    if text == "C":
        action = clear_display
    elif text == "=":
        action = calculate
    elif text == "√":
        action = square_root
    elif text == "⌫":
        action = clear_last_entry
    elif text in ["x²", "(", ")", "%", "÷", "x", "—", "+", "•"]:
        action = (lambda charrr=text: update_display(charrr))
    else:
        action = (lambda charrr = text : update_display(charrr))

    bg_color = "Light green" if text != "=" else "aqua"
    tk.Button(root, text=text, font=("Lucida Handwriting", 13, "bold"), width=8, height=3, command=action, bg=bg_color, border=0).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

for i in range(8):
    root.grid_rowconfigure(i, weight=1, minsize=60)
for i in range(4):
    root.grid_columnconfigure(i, weight=1, minsize=60)

root.mainloop()