from tkinter import *
import customtkinter
import openai
import os
import pickle


# Initiate App
root = customtkinter.CTk()
root.title('Chatopia')
root.geometry('800x600')
root.iconbitmap('ai_lt.ico')

# Set Color Scheme