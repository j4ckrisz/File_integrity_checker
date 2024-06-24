import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
  
  def __init__(self):
    super().__init__()
    # Configuring title, icon and size
    self.title('File Integrity Checker')
    #self.iconbitmap('images/logo.png')
    self.geometry('500x500')

# Widgets
    # Labels
    self.mylabel = ttk.Label(self, text='Write the file full path ', font=('Helvetica', 12))
    self.mylabel.pack(pady=20)

    # Buttons
    self.mybutton = ttk.Button(self, text='Compare')
    self.mybutton.pack(pady=20)

if __name__ == "__main__":
  app = App()
  app.mainloop()