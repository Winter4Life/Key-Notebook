
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from frame4 import open_frame4

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame6"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def validate_answer(username, password, answer):
    with open("accounts.txt", "r") as file:
        lines = file.readlines()
        accounts = [lines[i:i+4] for i in range(0, len(lines), 4)]
        for account in accounts:
            if account[0].strip() == username and account[1].strip() == password:
                if account[2].strip() == answer:
                    with open("current_user.txt", "a") as file:
                        file.write(f"{username}\n{password}\n")
                    window.destroy()
                    open_frame4()
                    return
                else:
                    messagebox.showerror("Error", "Incorrect answer")
                    return
                
def back() :
    from frame3 import open_frame3
    window.destroy()
    open_frame3()
                

def open_frame6(username, password):
    global window
    window = Tk()
    window.geometry("978x640")
    window.configure(bg="#DAD4BF")
    
    # Center window
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - 978) // 2
    y = (screen_height - 640) // 2
    window.geometry(f"+{x}+{y}")

    canvas = Canvas(
        window,
        bg="#DAD4BF",
        height=640,
        width=978,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
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

    canvas.create_rectangle(
        370.0,
        202.0,
        711.0,
        468.0,
        fill="#DAD4BF",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        525.5,
        366.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Andada Pro", 12)
    )
    entry_1.place(
        x=397.0,
        y=333.0,
        width=257.0,
        height=61.0,
    )

    # Read the accounts.txt file to find the corresponding question for the user
    question = None
    with open("accounts.txt", "r") as file:
        lines = file.readlines()
        accounts = [lines[i:i+4] for i in range(0, len(lines), 4)]
        for account in accounts:
            if account[0].strip() == username and account[1].strip() == password:
                question = account[3].strip()
                break

    if question is None:
        messagebox.showerror("Error", "verification failed")
        window.destroy()
        return

    canvas.create_text(
        522.0,
        230.0,
        anchor="center",
        text=f"{question}",
        fill="#000000",
        font=("AndadaProRoman Regular", 20 * -1)
    )

    def validate():
        validate_answer(username, password, entry_1.get())

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=validate,
        relief="flat"
    )
    button_1.place(
        x=405.0,
        y=487.0,
        width=244.0,
        height=67.0
    )
    button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
    frame6_back_button = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back(),
        relief="flat"
    )
    frame6_back_button.place(
        x=16.0,
        y=584.0,
        width=42.0,
        height=42.0
    )
    window.resizable(False, False)
    window.mainloop()