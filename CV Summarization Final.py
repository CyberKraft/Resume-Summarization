import spacy
import sys, fitz
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw

file_path = filedialog.askopenfilename()

fname = file_path
doc = fitz.open(fname)
text = ""
for page in doc:
    text = text + str(page.getText())

tx = " ".join(text.split('\n'))
#print(tx)

nlp_model = spacy.load('nlp_model')
doc = nlp_model(tx)
for ent in doc.ents:
    print(f'{ent.label_.upper():{30}}- {ent.text}')