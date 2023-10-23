import tkinter as tk

def append_to_output(value):
    current_text = output.get()
    output.delete(0, tk.END)
    output.insert(tk.END, current_text + value)

def clear_output():
    output.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(output.get())
        output.delete(0, tk.END)
        output.insert(tk.END, str(result))
    except Exception as e:
        output.delete(0, tk.END)
        output.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

output = tk.Entry(root, width=20, font=("Arial", 24))
output.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 18),
              command=lambda b=button: append_to_output(b) if b != '=' else calculate_result() if b == '=' else clear_output()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
