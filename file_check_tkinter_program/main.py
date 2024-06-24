import tkinter as tk
from tkinter import messagebox
import hashlib
import os

def calculate_md5(file_path):

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No such file: '{file_path}'")

    md5_hash = hashlib.md5()

    with open(file_path, "rb") as file:
        
        for chunk in iter(lambda: file.read(4096), b""):
            
            md5_hash.update(chunk)
    
    return md5_hash.hexdigest()

def on_button_click():

    file_path = file_path_entry.get()
    expected_md5 = expected_md5_entry.get()

    try:
        
        calculated_md5 = calculate_md5(file_path)
        
        if calculated_md5 == expected_md5:
        
            messagebox.showinfo("MD5 Check", "The MD5 hash matches!")
        
        else:
        
            messagebox.showwarning("MD5 Check", f"MD5 mismatch!\nExpected: {expected_md5}\nCalculated: {calculated_md5}")
    
    except FileNotFoundError as e:
        
        messagebox.showerror("File Error", str(e))
    
    except Exception as e:
        
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("MD5 Hash Checker")
root.geometry("400x200")


tk.Label(root, text="File Path:").pack(pady=5)
file_path_entry = tk.Entry(root, width=50)
file_path_entry.pack(pady=5)


tk.Label(root, text="Expected MD5 Hash:").pack(pady=5)
expected_md5_entry = tk.Entry(root, width=50)
expected_md5_entry.pack(pady=5)


check_button = tk.Button(root, text="Check MD5", command=on_button_click)
check_button.pack(pady=20)

root.mainloop()
