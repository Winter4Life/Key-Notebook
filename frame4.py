# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

# notebook page
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from frame5 import open_frame5
from cryptography.fernet import Fernet

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame4"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def load_key(filename):
    filepath = f"user_information/{filename}"
    with open(filepath, 'rb') as key_file:
        key = key_file.read()
    return key

def save_entries(entries, filename, key):
    filepath = f"user_information/{filename}"
    with open(filepath, 'wb') as file:
        for entry in entries:
            encrypted_entry = encrypt_text(entry.get(), key)
            file.write(encrypted_entry + b'\n')

def encrypt_text(text, key):
    cipher = Fernet(key)
    return cipher.encrypt(text.encode())

def decrypt_text(encrypted_text, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_text).decode()

def open_settings(entries, filename, key):
    save_entries(entries, filename, key)
    window.destroy()
    open_frame5()

# Function to read entry contents from a text file
def load_entries(entries, filename, key):
    filepath = f"user_information/{filename}"
    cipher = Fernet(key)
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                decrypted_line = decrypt_text(line, key)
                entries[i].insert(0, decrypted_line.strip())
    except FileNotFoundError:
        with open(filepath, 'w'):
            pass

def getUser():
    with open("current_user.txt", "r") as file:
        user = file.readline()
        return user.strip()

key = 0
entry_Dictionary = {}

def next_page(entries):
    global key
    global entry_Dictionary
    entryList = []
    count = count_entries(entries)
    if count == 40 and key == len(entry_Dictionary) - 1:
        for entry in entries:
            text = entry.get()
            entryList.append(text)
            entry.delete(0, 'end')
        entry_Dictionary[key] = entryList
        key += 1  # Move to the next page
    elif key < len(entry_Dictionary) - 1:
        if key < len(entry_Dictionary) - 1:
            key += 1
            next_entries = entry_Dictionary[key]
            for entry_widget, text in zip(entries, next_entries):
                entry_widget.delete(0, 'end')
                entry_widget.insert(0, text)

def previous_page(entries):
    global entry_Dictionary
    global key

    entryList = [entry.get() for entry in entries]
    entry_Dictionary[key] = entryList

    if key > 0:
        key -= 1
        previous_entries = entry_Dictionary[key] 
        for entry_widget, text in zip(entries, previous_entries):
            entry_widget.delete(0, 'end') 
            entry_widget.insert(0, text)

def show_journal():
    global entry_Dictionary
    for key, entries in entry_Dictionary.items():
        print(f"Page {key}:")
        for entry in entries:
            print(entry)

def count_entries(entries):
    count = 0
    for entry in entries:
        text = entry.get()
        if len(text) > 0:
            count += 1
    return count

# Frontend
def open_frame4():
    global window
    window = Tk()
    window.geometry("978x640")
    window.configure(bg = "#DAD4BF")
    
    # Center window
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - 978) // 2
    y = (screen_height - 640) // 2
    window.geometry(f"+{x}+{y}")
    
    entries = []
    name = getUser()
    key = load_key(name + "key.txt")

    canvas = Canvas(
        window,
        bg = "#DAD4BF",
        height = 640,
        width = 978,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        74.0,
        640.0,
        fill="#C3C3A9",
        outline="")

    canvas.create_rectangle(
        0.0,
        0.0,
        978.0,
        67.0,
        fill="#B5B59D",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        37.0,
        33.0,
        image=image_image_1
    )

    canvas.create_text(
        74.0,
        16.0,
        anchor="nw",
        text="Key Notebook",
        fill="#000000",
        font=("Amaranth Regular", 32 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    settings_button = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_settings(entries, name+".txt", key),
        relief="flat"
    )
    settings_button.place(
        x=16.0,
        y=590.0,
        width=42.0,
        height=42.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    notebook_button1 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    notebook_button1.place(
        x=15.0,
        y=83.0,
        width=45.0,
        height=45.0
    )

    canvas.create_rectangle(
        531.0,
        124.0,
        532.0000000803772,
        590.0,
        fill="#000000",
        outline="")
    coordinates_sets = [(198.0, 127.0,), (198.0, 220.0), (196.0, 313.0),
                        (196.0, 406.0) ,  (196.0, 499.0), (599.0,313.0),
                        (599.0, 406.0), (599.0, 499.0),(599.0, 220.0,) ,
                        (599.0, 127.0)]

    for coord in coordinates_sets:
        x, y = coord
        canvas.create_text(
            x,
            y,
            anchor="nw",
            text="Website\nEmail\nUsername\nPassword",
            fill="#000000",
            font=("Amaranth Regular", 16 * -1)
        )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=918.0,
        y=315.0,
        width=53.0,
        height=65.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=80.0,
        y=320.0,
        width=53.0,
        height=59.0
    )
    
    
    startImgx = 390.0
    startImgy = 137.0
    counter = 0
    for i in range(21):
        if counter == 4:
            startImgy += 17
            counter == 0
        entry_image = PhotoImage(file=relative_to_assets("entry_6.png"))
        entry_bg_6 = canvas.create_image(
            startImgx,
            startImgy,
            image=entry_image
        )
        startImgy += 19
        counter += 1
        
        
    startImgx = 791.0
    startImgy = 137.0
    counter == 0
    for i in range(21):
        if counter == 4:
            startImgy += 17
            counter == 0
        entry_image = PhotoImage(file=relative_to_assets("entry_6.png"))
        entry_bg_6 = canvas.create_image(
            startImgx,
            startImgy,
            image=entry_image
        )
        startImgy += 19


    startx = 277.0
    starty = 110.0
    for i in range(21):
        if i % 4 == 0:
            starty += 17
        entry = Entry(
            bd=0,
            bg="#DAD4BF",
            fg="#000716",
            highlightthickness=0
        )
        entry.place(
            x=startx,
            y=starty,
            width=226.0,
            height=13.0
        )
        starty += 19
        entries.append(entry)

    startx = 678.0
    starty = 110.0
    for i in range(21):
        if i % 4 == 0:
            starty += 17
        entry = Entry(
            bd=0,
            bg="#DAD4BF",
            fg="#000716",
            highlightthickness=0
        )
        entry.place(
            x=startx,
            y=starty,
            width=226.0,
            height=14.0
        )
        starty += 19
        entries.append(entry)


    canvas.create_rectangle(
        276.5,
        143.5000228881836,
        503.0,
        142.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        162.5000228881836,
        503.0,
        161.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        181.5000228881836,
        503.0,
        180.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        200.5000228881836,
        503.0,
        199.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        143.5000228881836,
        904.0,
        142.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        162.5000228881836,
        904.0,
        161.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        181.5000228881836,
        904.0,
        180.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        200.5000228881836,
        904.0,
        199.038818359375,
        fill="#000000",
        outline="")


    canvas.create_rectangle(
        677.5,
        235.5000228881836,
        904.0,
        234.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        254.5000228881836,
        904.0,
        253.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        273.5000228881836,
        904.0,
        272.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        292.5000228881836,
        904.0,
        291.038818359375,
        fill="#000000",
        outline="")


    canvas.create_rectangle(
        677.5,
        328.5000228881836,
        904.0,
        327.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        347.5000228881836,
        904.0,
        346.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        366.5000228881836,
        904.0,
        365.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        385.5000228881836,
        904.0,
        384.038818359375,
        fill="#000000",
        outline="")



    canvas.create_rectangle(
        677.5,
        421.5000228881836,
        904.0,
        419.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        440.5000228881836,
        904.0,
        438.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        459.5000228881836,
        904.0,
        457.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        478.5000228881836,
        904.0,
        476.038818359375,
        fill="#000000",
        outline="")


    canvas.create_rectangle(
        677.5,
        514.5000228881836,
        904.0,
        513.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        533.5000228881836,
        904.0,
        532.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        552.5000228881836,
        904.0,
        551.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        571.5000228881836,
        904.0,
        570.038818359375,
        fill="#000000",
        outline="")



    canvas.create_rectangle(
        276.5,
        236.5000228881836,
        503.0,
        235.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        255.5000228881836,
        503.0,
        254.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        274.5000228881836,
        503.0,
        273.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        293.5000228881836,
        503.0,
        292.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        329.5000228881836,
        503.0,
        328.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        348.5000228881836,
        503.0,
        347.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        367.5000228881836,
        503.0,
        366.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        386.5000228881836,
        503.0,
        385.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        421.5000228881836,
        503.0,
        420.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        440.5000228881836,
        503.0,
        439.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        459.5000228881836,
        503.0,
        458.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        478.5000228881836,
        503.0,
        477.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        514.5000228881836,
        503.0,
        513.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        533.5000228881836,
        503.0,
        532.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        552.5000228881836,
        503.0,
        551.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        571.5000228881836,
        503.0,
        570.038818359375,
        fill="#000000",
        outline="")

    def on_closing():
        save_entries(entries, name + ".txt", key)
        window.destroy()
        
    window.protocol("WM_DELETE_WINDOW", on_closing)
    load_entries(entries, name+".txt", key)
    window.resizable(False, False)
    window.mainloop()
