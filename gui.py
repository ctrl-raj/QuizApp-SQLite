import tkinter as tk

def submit():
    value = entry.get()
    print(f"Entry: {value}")
    label.config(text=f"Hello, {value}!")

# Initialize window
root = tk.Tk()
root.title("Tkinter Test")
root.geometry("300x150")

# Label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=5)

# Entry
entry = tk.Entry(root)
entry.pack(pady=5)

# Button
button = tk.Button(root, text="Submit", command=submit)
button.pack(pady=10)

# Run the app
root.mainloop()
