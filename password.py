import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    # Combine all possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the pool
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def show_password():
    # Get the desired password length from the entry field
    length = int(entry.get())
    
    # Generate the password
    password = generate_password(length)
    
    # Display the password in a message box
    messagebox.showinfo("Generated Password", f"Your password is:\n{password}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create an entry field for the user to input the desired password length
tk.Label(root, text="Enter password length:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

# Create a button to generate and display the password
tk.Button(root, text="Generate Password", command=show_password).pack(pady=20)

# Run the application
root.mainloop()
