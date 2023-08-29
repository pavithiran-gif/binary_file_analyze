import tkinter as tk
from tkinter import filedialog
import os

def convert_dat_to_file():
    dat_file_path = filedialog.askopenfilename(filetypes=[("DAT files", "*.dat")])
    if dat_file_path:
        with open(dat_file_path, 'r') as dat_file:
            hex_data = dat_file.read()
            binary_data = hex_to_bin(hex_data)
            original_file_extension = ".png"  # Assume the original file type is PDF
            original_file_path = os.path.splitext(dat_file_path)[0] + original_file_extension
            with open(original_file_path, 'wb') as original_file:
                original_file.write(binary_data)
            result_label.config(text=f"Converted to: {original_file_path}")

def hex_to_bin(hex_data):
    hex_data = hex_data.replace(" ", "").replace("\n", "")
    binary_data = bytes.fromhex(hex_data)
    return binary_data

# Create the main window
root = tk.Tk()
root.title("DAT File Converter")

# Create a button to convert .dat file content
convert_button = tk.Button(root, text="Convert .dat to Original File", command=convert_dat_to_file)
convert_button.pack(pady=10)

# Create a label to display the conversion result
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

# Start the GUI event loop
root.mainloop()
