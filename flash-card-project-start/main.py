import tkinter
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None

try:
    data = pd.read_csv("data\words_to_learn.csv")
except:
    data = pd.read_csv(r"data\french_words.csv")
finally:
    vocabs_dict = data.to_dict(orient="records")
#print(vocabs_dict)
#[{'French': 'premier', 'English': 'first'}]
data_vocab = None

def generate_vocab():
    global data_vocab
    data_vocab = random.choice(vocabs_dict)

def fr_vocabulary():
    global timer
    global data_vocab
    generate_vocab()
    #{'French': 'premier', 'English': 'first'}
    fr_vocab = data_vocab['French']
    timer = window.after(3000, flip_card)
    return fr_vocab

def en_vocabulary():
    global data_vocab
    en_vocab = data_vocab["English"]
    return en_vocab

def flip_card():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_image, image=green_bg)
    canvas.itemconfig(fr_title, text="English", font=("Ariel", 40, "italic"), fill="white")
    canvas.itemconfig(fr_word, text=en_vocabulary(), fill= "white")

def next_vocabulary():
    next_vocab = fr_vocabulary()
    canvas.itemconfig(canvas_image, image=white_bg)
    canvas.itemconfig(fr_title, text="French", font=("Ariel", 40, "italic"), fill="black")
    canvas.itemconfig(fr_word, text=next_vocab, fill="black")
    save_to_file(data_vocab)

def save_to_file(vocab):
    vocabs_dict.remove(vocab)
    df = pd.DataFrame(vocabs_dict)
    df.to_csv("words_to_learn.csv", index=False)





#-------------------------------------------------------------------
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
white_bg = tkinter.PhotoImage(file="images\card_front.png")
canvas_image = canvas.create_image(410, 273, image=white_bg)
fr_title = canvas.create_text(410, 150, text="French", font=("Ariel", 40, "italic"))
fr_word = canvas.create_text(400, 263, text=fr_vocabulary(), font=("Ariel", 60, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

green_bg = tkinter.PhotoImage(file="images\card_back.png")


cancel_img = tkinter.PhotoImage(file="images\wrong.png")
cancel_button = tkinter.Button(image=cancel_img, highlightthickness=0, command=next_vocabulary)
mark_img = tkinter.PhotoImage(file=r"images\right.png")
mark_button = tkinter.Button(image=mark_img, highlightthickness=0, command=next_vocabulary)
cancel_button.grid(column=0, row=1)
mark_button.grid(column=1, row=1)

window.mainloop()
