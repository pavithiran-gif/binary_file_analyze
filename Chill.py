import tkinter as tk
from tkinter import filedialog
import magic
import os

def get_file_type(filename):
    mime = magic.Magic()
    return mime.from_file(filename)

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_type = get_file_type(file_path)
        result_label.config(text=f"File Type: {file_type}")
        generate_dat_button.config(state=tk.NORMAL)
        detect_dat_button.config(state=tk.DISABLED)
        selected_file_path.set(file_path)

def detect_dat_file():
    dat_file_path = filedialog.askopenfilename(filetypes=[("DAT files", "*.dat")])
    if dat_file_path:
        file_type = get_file_type(dat_file_path)
        result_label.config(text=f"DAT File Type: {file_type}")

def generate_dat_file():
    input_file_path = selected_file_path.get()
    if input_file_path:
        with open(input_file_path, 'rb') as input_file:
            binary_data = input_file.read()  # Read the file content as binary data
            base_name = os.path.splitext(os.path.basename(input_file_path))[0]
            dat_file_path = os.path.join("gen", base_name + ".dat")
            os.makedirs(os.path.dirname(dat_file_path), exist_ok=True)
            with open(dat_file_path, 'wb') as dat_file:
                dat_file.write(binary_data)  # Write the binary data to the .dat file
            result_label.config(text=f"Generated .dat file: {dat_file_path}")
            generate_dat_button.config(state=tk.DISABLED)
            detect_dat_button.config(state=tk.NORMAL)

# Create the main window
root = tk.Tk()
root.title("File Converter and Type Detector")

# Create variables to store selected file path
selected_file_path = tk.StringVar()

# Create a button to browse for a file
browse_button = tk.Button(root, text="Browse and Detect Type", command=browse_file)
browse_button.pack(pady=10)

# Create a button to detect .dat file type
detect_dat_button = tk.Button(root, text="Detect .dat File Type", command=detect_dat_file, state=tk.DISABLED)
detect_dat_button.pack(pady=10)

# Create a label to display the selected file type result
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

# Create a button to generate .dat file
generate_dat_button = tk.Button(root, text="Generate .dat File", command=generate_dat_file, state=tk.DISABLED)
generate_dat_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
