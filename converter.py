'''
Image Converter 
Created By: Ivan Brix A Olaguir
Free To Use
Open Source
'''

# Imports
from tkinter import*
from PIL import Image, ImageTk
import webbrowser
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import os

# Screen
root = Tk()
root.title("Ibao Image Converter")
root.geometry("400x200")
root.configure(bg="#5d5e5c")
root.resizable(0,0)
root.iconbitmap("C:\\Users\\Nap\\Desktop\\Python project\\icon\\iconconverter.ico")

# Label Screen
label = Label(root, width=50, height=1, bg='#59ff00', fg="black", relief='sunken', bd=2, justify="left")
label.pack(pady=5, anchor=CENTER)

my_label = Label(root, text="Welcome User", fg='cyan', bg='black', font=("BOLD"), relief="sunken")
my_label.pack(pady=10)

label_1 = Label(root, width=50, height=1, bg='#59ff00', fg="black", relief='sunken',)
label_1.pack(pady=1, anchor=CENTER)


# Functions
def source_code():
	webbrowser.open("https://github.com/settings/profile")

def show_image():
	global img
	filename = filedialog.askopenfilename(initialdir="C:\\", title="Select Image", filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.*")))
	img = Image.open(filename)
	img.thumbnail((200, 200))
	label.config(text=f'{img}')

	

def convert():
    global img
    try:
    	export = filedialog.asksaveasfilename(defaultextension='.*', title="Save Image As", filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("Icon File", "*.ico"), ("All Files", "*.*")))
    	img.save(export)
    	label_1.config(text=f'{img}')
    except:
    	messagebox.showerror("Ibao Image Converter", "Error: No File selected")


# Frame 
frame = Frame(root, bg="white")
frame.pack(side=BOTTOM, pady=10, padx=10)

convert_Button = Button(frame, text="Convert", width=10, height=0, bd=2, command=convert, fg="white", bg="skyblue", font=("Bold"))
convert_Button.pack()

def About():
	root = Tk()
	root.title("Ibao Image Converter")
	root.geometry("300x110")
	root.configure(bg="#000000")
	root.resizable(0,0)
	root.iconbitmap("C:\\Users\\Nap\\Desktop\\Python project\\icon\\iconconverter.ico")
	root.overrideredirect(False)
	Label(root, text="Created By: Ivan Brix A. Olaguir", font=("Helvetica", 15), fg="#fc0303").pack(pady=10)
	Button(root, text="Okay", width=10, height=0, bd=3, bg="#ff00ee", fg="white", command=lambda: root.destroy()).pack(pady=15)

	root.mainloop()

# Menu Bar 
menuBar = Menu(root)
root.config(menu=menuBar)

# File Menu
file_menu = Menu(menuBar, tearoff=False)
file_menu.add_separator()
file_menu.add_command(label="Open Image", command=show_image)
file_menu.add_command(label="Exit", command=lambda: root.destroy())
menuBar.add_cascade(labe="File", menu=file_menu)

# Help Menu
help_menu = Menu(menuBar, tearoff=False)
help_menu.add_separator()
help_menu.add_command(label="Source Code", command=source_code)
help_menu.add_command(label="About", command=About)
menuBar.add_cascade(labe="Help", menu=help_menu)

# Mainloop
root.mainloop()


# Thank you for using my program