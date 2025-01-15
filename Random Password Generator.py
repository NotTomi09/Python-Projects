import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_uppercase, use_digits, use_special):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special = '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    characters = lowercase
    if use_uppercase:
        characters += uppercase
    if use_digits:
        characters += digits
    if use_special:
        characters += special

    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def handle_generate():
    try:
        length = int(password_length.get()) 
        if length <= 0:
            raise ValueError("Password length must be positive.")
        use_uppercase = include_uppercase.get()
        use_digits = include_digits.get()
        use_special = include_special.get()

        
        password = generate_password(length, use_uppercase, use_digits, use_special)
        result_var.set(password)  # Display the password in the entry widget

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Password Length
tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
password_length = tk.Entry(root, width=5)
password_length.grid(row=0, column=1, padx=10, pady=5)

# Include Uppercase Letters
include_uppercase = tk.BooleanVar()
tk.Checkbutton(root, text="Include Uppercase Letters", variable=include_uppercase).grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)

# Include Digits
include_digits = tk.BooleanVar()
tk.Checkbutton(root, text="Include Digits", variable=include_digits).grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5)

# Include Special Characters
include_special = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=include_special).grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5)

# Generate Password Button
tk.Button(root, text="Generate Password", command=handle_generate).grid(row=4, column=0, columnspan=2, pady=10)

# Display Generated Password
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, state="readonly", width=30).grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Start the application
root.mainloop()

