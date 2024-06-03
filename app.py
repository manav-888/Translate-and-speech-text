from  gtts import gTTS
import os
from tkinter import *
from tkinter import  ttk
import tkinter as tk

from googletrans import Translator

root = Tk()

canvas = Canvas(root , width = 400 , height= 300)
canvas.pack()

def textToSpeech():
    text =entry.get()
    language = language_combo.get()
    output = gTTS(text=text, lang=language, slow=False)
    output.save('fileoutput.mp3')
    os.system('afplay fileoutput.mp3')

    translator = Translator()
    translation = translator.translate(text, dest="hi")  # Translate text to English
    translated_text.set(translation.text)  # Set translated text to the StringVar


entry = Entry(root)
canvas.create_window(200 ,150 ,window =entry)

button = Button(text = 'Start' , command=textToSpeech ,font=("Arial", 20))
canvas.create_window(200 ,250 ,window =button)

label =Label(root, text='Enter Text' ,font=("Arial", 25))
canvas.create_window(200 ,100 ,window =label )

# Translated Text Label
translated_text = tk.StringVar()
translated_label = tk.Label(root, textvariable=translated_text)
canvas.create_window(200 ,280 ,window =translated_label )

# language combo
languages = ["en", "fr", "es", "de",'hi']  # Add more languages as needed
language_combo = ttk.Combobox(root, values=languages)
canvas.create_window(200 ,200 ,window =language_combo )


root.mainloop()



