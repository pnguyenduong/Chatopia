from tkinter import *
import customtkinter
import openai
import os
import pickle


# Initiate App
root = customtkinter.CTk()
root.title('Chatopia')
root.geometry('800x600')

# Set Color Scheme
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# Create Text Frame
frame = customtkinter.CTkFrame(master=root,
                               width=400,
                               height=300,
                               corner_radius=10)
frame.pack(padx=(20, 100), pady=(300, 20))

# Add Text Widget to get ChatGPT Responses
textbox = customtkinter.CTkTextbox(frame)
textbox.grid(row=0, column=0)
textbox.configure(
    text_color='black',
    width=600,
    height=400,
    fg_color='#d6d6d6',
    wrap=WORD,
    state='normal')

# Run the app
root.mainloop()