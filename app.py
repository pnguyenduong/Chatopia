from dotenv import load_dotenv
from tkinter import *
import customtkinter
import openai
import os

# load environment variable from .env file (API key)
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# initiate App
app = customtkinter.CTk()
app.title('Chatopia')
app.geometry('800x600')


# set color scheme
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue')


# send text to OpenAI api
def send():
    if chatbox.get():
        # define our api key to ChatGPT
        openai.api_key = OPENAI_API_KEY
        # create an instance
        openai.Model.list()
        # define our query / response
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = chatbox.get(),
            temperature = 0,
            max_tokens = 60,
            top_p = 1.0,
            logprobs=10,
        )
        textbox.insert(END, "You: " + chatbox.get())
        textbox.insert(END, "\n")
        textbox.insert(END, ("ChatGPT: " + response["choices"][0]["text"].strip()))
        textbox.insert(END, "\n")
        chatbox.delete(0, END)
        
    else:
        textbox.insert(END, "\nYou didn't type anything!")
        


# clear the text on screen
def clear():
    # clear textbox
    textbox.delete(1.0, END)
    #clear chatentry
    chatbox.delete(0, END)


# create text frame
frame = customtkinter.CTkFrame(
    app,
    width=400,
    height=300,
    corner_radius=10
)
frame.pack(padx=(20), pady= (20))


# add text widget to display ChatGPT responses
textbox = customtkinter.CTkTextbox(frame)
textbox.grid(row=0, column=0)
textbox.configure(
    text_color='black',
    width=600,
    height=400,
    fg_color='#d6d6d6',
    wrap=WORD,
    state='normal'
)


# add entry widget to type stuff to ChatGPT
chatbox = customtkinter.CTkEntry(
    app, 
    placeholder_text='Type something to OpenAI',
    width=400,
    height=50,
    border_width=2
)
chatbox.pack(pady=10)


# create button frame
button_frame = customtkinter.CTkFrame(
    app,
    width=200,
    height=50,
)
button_frame.pack(pady=10)


# create send buttons
send_button = customtkinter.CTkButton(
    button_frame,
    text="Send",
    command=send
)
send_button.grid(row=0, column=0, padx=25)


# create clear buttons
clear_button = customtkinter.CTkButton(
    button_frame,
    text="Clear",
    command=clear
)
clear_button.grid(row=0, column=1, padx=25)


# run the app
app.mainloop()