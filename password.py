# PASSWORD GENERATOR 


import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password has at least one character from each category
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length-4)
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

def generate_password_button():
    try:
        length = int(entry.get())
        password = generate_password(length)
        result_label.config(text=f"Generated password: {password}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
tk.Label(root, text="Enter password length:").grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password_button)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
