# Importing Modules Needed For Application
import tkinter as tk
import math, random

# Function to generate password
def generatePassword():
 
    # Declare all the variables that can be used in string
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-?'
    password = ""
    length = len(string)
    for i in range(16) :
        password += string[math.floor(random.random() * length)]
        label.config(text=password)
    
    return password

def copy2clip():
  x = generatePassword()
  root.clipboard_clear()
  root.clipboard_append(x)
  root.update()


# -----------------------------  UI Configuration  ---------------------------------
root = tk.Tk()
root.geometry("300x200")
root.title("X-Pass: Password Generator")

button = tk.Button(root, text = "Generate Password", command = copy2clip)
button.pack(pady = 20)

label = tk.Label(root, font=('times', 15, "bold"))
label.pack(pady = 20)

root.mainloop()