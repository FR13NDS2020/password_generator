import random
import string
import tkinter as tk
import pyperclip


def generate_password(length, include_lower=True, include_upper=True, include_numbers=True, include_symbols=True):
    letters = ""
    if include_lower:
        letters += string.ascii_lowercase
    if include_upper:
        letters += string.ascii_uppercase
    if include_numbers:
        letters += string.digits
    if include_symbols:
        letters += string.punctuation

    password = "".join(random.choice(letters) for i in range(length))
    return password


def generate_button_click():
    length = length_entry.get()
    try:
        length = int(length)
    except ValueError:
        password_label.config(text="Please enter a valid integer")
        return

    if length <= 0:
        password_label.config(text="Please enter a positive integer")
        return

    include_lower = lower_var.get()
    include_upper = upper_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()

    if not include_lower and not include_upper and not include_numbers and not include_symbols:
        password_label.config(text="Please select at least one character set")
        return

    password = generate_password(length, include_lower, include_upper, include_numbers, include_symbols)
    password_label.config(text=password)
    pyperclip.copy(password)


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x500")
root.configure(bg="#f0f0f0")
root.resizable(False, False)


title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 24), bg="#f0f0f0")
title_label.pack(pady=20)


length_frame = tk.Frame(root, bg="#f0f0f0")
length_frame.pack()

length_label = tk.Label(length_frame, text="Password Length: ", font=("Helvetica", 12), bg="#f0f0f0")
length_label.pack(side=tk.LEFT, padx=10, pady=10)

length_entry = tk.Entry(length_frame, width=4, font=("Helvetica", 12))
length_entry.pack(side=tk.LEFT, padx=10, pady=10)


charset_label = tk.Label(root, text="Character Sets:", font=("Helvetica", 12), bg="#f0f0f0")
charset_label.pack(pady=10)

lower_var = tk.BooleanVar()
lower_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var, font=("Helvetica", 10), bg="#f0f0f0")
lower_check.pack()

upper_var = tk.BooleanVar()
upper_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var, font=("Helvetica", 10), bg="#f0f0f0")
upper_check.pack()

numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, font=("Helvetica", 10), bg="#f0f0f0")
numbers_check.pack()

symbols_var = tk.BooleanVar()
symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, font=("Helvetica", 10), bg="#f0f0f0")
symbols_check.pack()


generate_button = tk.Button(root, text="Generate Password", command=generate_button_click, font=("Helvetica", 12),
                            bg="#F7A072", fg="white", pady=10, padx=20)
generate_button.pack(pady=20)

password_frame = tk.Frame(root, bg="#f0f0f0")
password_frame.pack(pady=10)

password_label = tk.Label(password_frame, text="", font=("Helvetica", 12), bg="#d1d1d1", pady=10, padx=20, width=30, height=1, relief="sunken", bd=2)
password_label.pack()

copy_button = tk.Button(password_frame, text="Copy to Clipboard", command=lambda: pyperclip.copy(password_label["text"]),
font=("Helvetica", 10), bg="#F7A072", fg="white", padx=10, pady=5)
copy_button.pack(pady=10)


length_entry.focus()

root.mainloop()
