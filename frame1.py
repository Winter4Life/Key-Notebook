
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage
from frame2 import open_frame2
from frame3 import open_frame3

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame1"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Frontend
def open_frame1():
    window = Tk()
    window.geometry("978x640")
    window.configure(bg = "#DAD4BF")
    
    # Button functions
    def create_account_clicked():
        window.destroy()  # Close current window
        open_frame2()     # Open frame2

    def login_clicked():
        window.destroy()  # Close current window
        open_frame3()     # Open frame3

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
    frame1_createAcc_button = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=create_account_clicked,
        relief="flat",
        
    )
    frame1_createAcc_button.place(
        x=210.0,
        y=409.0,
        width=271.0,
        height=86.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    frame1_Login_button = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=login_clicked,
        relief="flat"
    )
    frame1_Login_button.place(
        x=560.0,
        y=409.0,
        width=270.0,
        height=80.0
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
        x=456.0,
        y=515.0,
        width=128.0,
        height=29.0
    )

    canvas.create_text(
        395.0,
        203.0,
        anchor="nw",
        text="Create Account\nor\nLogin",
        fill="#000000",
        font=("RobotoSerifNormalRoman Regular", 36 * -1),
        justify="center"
    )
    window.resizable(False, False)
    window.mainloop()