from tkinter import *
from password_generator import PasswordGenerator
from data_manager import DataManager
import pyperclip

class PasswordManagerUI():
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)
        
        self.setup_ui()
        self.window.mainloop()
    
    def setup_ui(self):
        #Canvas
        self.canvas = Canvas(height=200, width=200)
        self.logo_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(row=0, column=1)
        
        #Labels
        Label(text="Website:").grid(row=1, column=0, sticky=EW)
        Label(text="Email/Username:").grid(row=2, column=0)
        Label(text="Password:").grid(row=3, column=0, sticky=EW)
        
        #Entries
        self.website_entry = Entry(width=35)
        self.website_entry.grid(row=1, column=1, columnspan=2, sticky=EW)
        self.website_entry.focus()
        
        self.email_entry = Entry(width=35)
        self.email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
        self.email_entry.insert(0, "common@email.com")
        
        self.password_entry = Entry(width=18)
        self.password_entry.grid(row=3, column=1, sticky=EW)
        
        #Buttons
        Button(text="Generate Password", width=14, command=self.generate_password).grid(row=3, column=2, sticky=EW)
        Button(text="Add", width=32, command=self.save).grid(row=4, column=1, columnspan=2, sticky=EW)
        
    def generate_password(self):
        password = PasswordGenerator.generate()
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)
        
    def save(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        if DataManager.save(website, email, password):
            self.website_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.website_entry.focus()