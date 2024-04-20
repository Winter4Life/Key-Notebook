
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, messagebox, Button, PhotoImage
from frame4 import open_frame4


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame2"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Function to check if the account information exists
def validate_existence(username, password):
    with open("accounts.txt", "r") as file:
        lines = file.readlines()
        # Combine lines into pairs of username-password
        accounts = [lines[i:i+2] for i in range(0, len(lines), 2)]
        for account in accounts:
            if account[0].strip() == username and account[1].strip() == password:
                return False
    return True

def submit_butt(username, password):
    if validate_existence(username, password):
        messagebox.showerror("Error", "Account does not exists")
        return
    
    window.destroy()
    open_frame4()

# Frontend
def open_frame3():
    global window
    window = Tk()
    window.geometry("978x640")
    window.configure(bg = "#DAD4BF")


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
        526.5,
        395.5,
        image=entry_image_1
    )
    frame3_password = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Andada Pro", 12),
        show="*"
    )
    frame3_username = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Andada Pro", 12),
        
    )
    frame3_username.place(
        x=398.0,
        y=237.0,
        width=257.0,
        height=61.0
    )
    frame3_password.place(
        x=398.0,
        y=363.0,
        width=257.0,
        height=61.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        526.5,
        270.0,
        image=entry_image_2
    )

    canvas.create_text(
        487.0,
        125.0,
        anchor="nw",
        text="Login",
        fill="#000000",
        font=("RobotoSerifNormalRoman Regular", 36 * -1)
    )

    canvas.create_text(
        402.0,
        220.0,
        anchor="nw",
        text="email or username",
        fill="#000000",
        font=("AndadaProRoman Regular", 13 * -1)
    )

    canvas.create_text(
        402.0,
        345.0,
        anchor="nw",
        text="password",
        fill="#000000",
        font=("AndadaProRoman Regular", 13 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    frame3_submit_button = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: submit_butt(frame3_username.get(), frame3_password.get()),
        relief="flat"
    )
    frame3_submit_button.place(
        x=405.0,
        y=479.0,
        width=244.0,
        height=67.0
    )
    window.resizable(False, False)
    window.mainloop()