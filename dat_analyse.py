import tkinter as tk
from tkinter import filedialog
import magic

def get_file_type(filename):
    mime = magic.Magic()
    return mime.from_file(filename)

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_type = get_file_type(file_path)
        result_label.config(text=f"Detected File Type: {file_type}")

# Create the main window
root = tk.Tk()
root.title("File Type Detector")

# Create a label for instructions
instruction_label = tk.Label(root, text="Please select a file:")
instruction_label.pack(pady=10)

# Create a button to browse for a file
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

# Create a label to display the detected file type
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

# Start the GUI event loop
root.mainloop()
