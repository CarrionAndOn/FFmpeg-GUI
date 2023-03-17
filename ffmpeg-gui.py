import tkinter as tk
from tkinter import ttk, filedialog
import subprocess
import sys
import os

root = tk.Tk()
root.title("FFmpeg")
root.geometry("397x148")

# Get the script's filename and extract its base name (without the extension)
script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
# This avoids the script breaking if the user changes the file name
root.iconbitmap(f"{script_name}.exe")

# Override the background color of the root window to use the breeze dark theme
root.configure(background='#3b3f4c')

# Use the 'alt' theme for ttk widgets
style = ttk.Style(root)
style.theme_use('clam')

# Override the background color of all widgets to use the breeze dark theme
style.map("TButton", background=[('active', '#3daee9'), ('!disabled', '#3b3f4c')], foreground=[('!disabled', '#d8d8d8')])
style.map("TEntry", background=[('disabled','#555'), ('!disabled', '#3b3f4c')], foreground=[('disabled', '#ccc'), ('!disabled', '#d8d8d8')])
style.map("TLabel", background=[('!disabled', '#3b3f4c')], foreground=[('!disabled', '#d8d8d8')])
style.map("TCombobox", background=[('disabled','#555'), ('!disabled', '#3b3f4c')], foreground=[('disabled', '#ccc'), ('!disabled', '#d8d8d8')])
style.map("TCheckbutton", background=[('!disabled', '#3b3f4c')], foreground=[('!disabled', '#d8d8d8')])
style.configure("TFrame", background='#3b3f4c')
style.configure("TNotebook", background='#3b3f4c')

input_file_path = ""
output_file_path = ""

def select_input_file():
    global input_file_path
    input_file_path = filedialog.askopenfilename()
    input_file_label.config(text=input_file_path)

def select_output_file():
    global output_file_path
    output_file_path = filedialog.asksaveasfilename()
    output_file_label.config(text=output_file_path)

def convert_file():
    if not input_file_path:
        status_label.config(text="Please select input file")
        return
    if not output_file_path:
        status_label.config(text="Please select output file")
        return
    command = f'ffmpeg -i "{input_file_path}" "{output_file_path}"'
    subprocess.call(command, shell=True)
    status_label.config(text="Conversion successful!")

input_file_button = ttk.Button(root, text="Select input file", command=select_input_file)
input_file_button.pack()

input_file_label = ttk.Label(root, text="No input file selected")
input_file_label.pack()

output_file_button = ttk.Button(root, text="Select output file", command=select_output_file)
output_file_button.pack()

output_file_label = ttk.Label(root, text="No output file selected")
output_file_label.pack()

convert_button = ttk.Button(root, text="Convert file", command=convert_file)
convert_button.pack()

status_label = ttk.Label(root, text="")
status_label.pack()

root.mainloop()
