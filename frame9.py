
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame9"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    378.0,
    207.0,
    719.0,
    615.0,
    fill="#DAD4BF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    534.5,
    390.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Andada Pro", 12),
)
entry_1.place(
    x=406.0,
    y=358.0,
    width=257.0,
    height=61.0
)

canvas.create_text(
    400.0,
    130.0,
    anchor="nw",
    text="Forgot Password",
    fill="#000000",
    font=("RobotoSerifNormalRoman Regular", 36 * -1)
)

canvas.create_text(
    410.0,
    340.0,
    anchor="nw",
    text="enter answer",
    fill="#000000",
    font=("AndadaProRoman Regular", 13 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
submit_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
submit_button.place(
    x=413.0,
    y=491.0,
    width=244.0,
    height=67.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
back_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
back_button.place(
    x=16.0,
    y=582.0,
    width=42.0,
    height=42.0
)

canvas.create_text(
    500.0,
    249.0,
    anchor="nw",
    text="question\n",
    fill="#000000",
    font=("AndadaProRoman Regular", 13 * -1)
)
window.resizable(False, False)
window.mainloop()
