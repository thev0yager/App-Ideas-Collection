import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry("300x150")
root.resizable(False, False)
root.title('Binary 2 Decimal Converter')

# function value
value = tk.StringVar()

# binary conversion & error handling
def bin2dec():
    
    for i in value.get():
        if i in '10':
            continue
        else:
            showinfo(title='Error', message='Not binary digits')
            exit()
    
    if len(value.get()) > 8:
        showinfo(title='Error', message='Wrong number of digits')
        exit()
    else:
        binNum = int(value.get())
        decNum = 0
        power = 0

        while binNum > 0 and power < 8:
            decNum += 2 ** power * (binNum % 10)
            binNum //= 10
            power += 1
        
        msg = f'Your converted value is: {decNum}'
        showinfo(title='Results', message=msg)

# app frame
app = ttk.Frame(root)
app.pack(padx=10, pady=10, fill='x', expand=True)

# input value label
value_label = ttk.Label(app, text="Enter Binary String: ")
value_label.pack(fill='x', expand=True)

# input entry field
value_entry = ttk.Entry(app, width=8, textvariable=value)
value_entry.pack(fill='x', expand=True)
value_entry.focus()

# submit button
submit_button = ttk.Button(app, text="Submit", command=bin2dec)
submit_button.pack(fill='x', expand=True, pady=10)

root.mainloop()