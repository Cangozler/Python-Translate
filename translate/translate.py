from cProfile import label
from tkinter import *
from turtle import left
import googletrans
from matplotlib.pyplot import grid
import textblob
from tkinter import ttk, messagebox



root = Tk()
root.title('Simple Translate')
root.geometry("627x251")
root.configure(background="azure2")
canvas= Canvas(root, width= 1000, height= 750, bg="SpringGreen2")
dwnd = PhotoImage(file='bb.png')
dwndd = PhotoImage(file='aa.png')
def translate_it():
	translated_text.delete(1.0, END)
	try:
		for key, value in languages.items():
			if (value == original_combo.get()):
				from_language_key = key
		for key, value in languages.items():
			if (value == translated_combo.get()):
				to_language_key = key

		words = textblob.TextBlob(original_text.get(1.0, END))
		words = words.translate(from_lang=from_language_key , to=to_language_key)
		translated_text.insert(10.0, words)
	except Exception as e:
		messagebox.showerror("Translator", e)
def clear():
	original_text.delete(1.0, END)
	translated_text.delete(1.0, END)

languages = googletrans.LANGUAGES
language_list = list(languages.values())



original_text = Text(root, height=4, width=25)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, image=dwnd, text="Translate!", font=("Helvetica", 12), command=translate_it)
translate_button.grid(row=1, column=0, padx=1)

translated_text = Text(root, height=4, width=25)
translated_text.grid(row=0, column=2, pady=0, padx=1)


translated_combo = ttk.Combobox(root, width=8, value=language_list)
translated_combo.current(20)
translated_combo.grid(row=0, pady=0, padx=0, ipadx=100, sticky=(W,N), column=2)

original_combo = ttk.Combobox(root, width=8, value=language_list)
original_combo.current(21)
original_combo.grid(row=0, pady=0, padx=0, ipadx=100, sticky=(W,N), column=0)


clear_button = Button(root, image=dwndd,text="I can Clear", command=clear)
clear_button.grid(row=1, pady=0, padx=10, column=2)
root.mainloop()