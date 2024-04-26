
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

# notebook page
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from frame5 import open_frame5

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame1"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_settings():
    window.destroy()
    open_frame5()

# Frontend
def open_frame4():
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

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    settings_button = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_settings(),
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

    canvas.create_text(
        198.0,
        127.0,
        anchor="nw",
        text="Website\nEmail\nUsername\nPassword",
        fill="#000000",
        font=("Amaranth Regular", 16 * -1)
    )

    canvas.create_text(
        198.0,
        220.0,
        anchor="nw",
        text="Website\nEmail\nUsername\nPassword",
        fill="#000000",
        font=("Amaranth Regular", 16 * -1)
    )

    canvas.create_text(
        196.0,
        313.0,
        anchor="nw",
        text="Website\nEmail\nUsername\nPassword",
        fill="#000000",
        font=("Amaranth Regular", 16 * -1)
    )

    canvas.create_text(
        196.0,
        406.0,
        anchor="nw",
        text="Website\nEmail\nUsername\nPassword",
        fill="#000000",
        font=("Amaranth Regular", 16 * -1)
    )

    canvas.create_text(
        196.0,
        499.0,
        anchor="nw",
        text="Website\nEmail\nUsername\nPassword",
        fill="#000000",
        font=("Amaranth Regular", 16 * -1)
    )

    canvas.create_text(
        599.0,
        313.0,
        anchor="nw",
        text="Website\nEmail\nUsername\nPassword",
        fill="#000000",
        font=("Amaranth Regular", 16 * -1)
    )

    canvas.create_text(
        599.0,
        406.0,
        anchor="nw",
        text="Website\nEmail\nUsername\nPassword",
        fill="#000000",
        font=("Amaranth Regular", 16 * -1)
    )

    canvas.create_text(
        599.0,
        499.0,
        anchor="nw",
        text="Website\nEmail\nUsername\nPassword",
        fill="#000000",
        font=("Amaranth Regular", 16 * -1)
    )

    canvas.create_text(
        599.0,
        220.0,
        anchor="nw",
        text="Website\nEmail\nUsername\nPassword",
        fill="#000000",
        font=("Amaranth Regular", 16 * -1)
    )

    canvas.create_text(
        599.0,
        127.0,
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

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        390.0,
        137.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=277.0,
        y=129.0,
        width=226.0,
        height=14.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        390.0,
        156.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=277.0,
        y=148.0,
        width=226.0,
        height=14.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        390.0,
        175.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=277.0,
        y=167.0,
        width=226.0,
        height=14.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        390.0,
        194.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=277.0,
        y=186.0,
        width=226.0,
        height=14.0
    )

    canvas.create_rectangle(
        276.5,
        141.5000228881836,
        503.0,
        142.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        160.5000228881836,
        503.0,
        161.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        179.5000228881836,
        503.0,
        180.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        198.5000228881836,
        503.0,
        199.038818359375,
        fill="#000000",
        outline="")

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        791.0,
        137.0,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=678.0,
        y=129.0,
        width=226.0,
        height=14.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        791.0,
        156.0,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=678.0,
        y=148.0,
        width=226.0,
        height=14.0
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        791.0,
        175.0,
        image=entry_image_7
    )
    entry_7 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_7.place(
        x=678.0,
        y=167.0,
        width=226.0,
        height=14.0
    )

    entry_image_8 = PhotoImage(
        file=relative_to_assets("entry_8.png"))
    entry_bg_8 = canvas.create_image(
        791.0,
        194.0,
        image=entry_image_8
    )
    entry_8 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_8.place(
        x=678.0,
        y=186.0,
        width=226.0,
        height=14.0
    )

    canvas.create_rectangle(
        677.5,
        141.5000228881836,
        904.0,
        142.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        160.5000228881836,
        904.0,
        161.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        179.5000228881836,
        904.0,
        180.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        198.5000228881836,
        904.0,
        199.038818359375,
        fill="#000000",
        outline="")

    entry_image_9 = PhotoImage(
        file=relative_to_assets("entry_9.png"))
    entry_bg_9 = canvas.create_image(
        791.0,
        229.0,
        image=entry_image_9
    )
    entry_9 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_9.place(
        x=678.0,
        y=221.0,
        width=226.0,
        height=14.0
    )

    entry_image_10 = PhotoImage(
        file=relative_to_assets("entry_10.png"))
    entry_bg_10 = canvas.create_image(
        791.0,
        248.0,
        image=entry_image_10
    )
    entry_10 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_10.place(
        x=678.0,
        y=240.0,
        width=226.0,
        height=14.0
    )

    entry_image_11 = PhotoImage(
        file=relative_to_assets("entry_11.png"))
    entry_bg_11 = canvas.create_image(
        791.0,
        267.0,
        image=entry_image_11
    )
    entry_11 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_11.place(
        x=678.0,
        y=259.0,
        width=226.0,
        height=14.0
    )

    entry_image_12 = PhotoImage(
        file=relative_to_assets("entry_12.png"))
    entry_bg_12 = canvas.create_image(
        791.0,
        286.0,
        image=entry_image_12
    )
    entry_12 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_12.place(
        x=678.0,
        y=278.0,
        width=226.0,
        height=14.0
    )

    canvas.create_rectangle(
        677.5,
        233.5000228881836,
        904.0,
        234.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        252.5000228881836,
        904.0,
        253.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        271.5000228881836,
        904.0,
        272.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        290.5000228881836,
        904.0,
        291.038818359375,
        fill="#000000",
        outline="")

    entry_image_13 = PhotoImage(
        file=relative_to_assets("entry_13.png"))
    entry_bg_13 = canvas.create_image(
        791.0,
        322.0,
        image=entry_image_13
    )
    entry_13 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_13.place(
        x=678.0,
        y=314.0,
        width=226.0,
        height=14.0
    )

    entry_image_14 = PhotoImage(
        file=relative_to_assets("entry_14.png"))
    entry_bg_14 = canvas.create_image(
        791.0,
        341.0,
        image=entry_image_14
    )
    entry_14 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_14.place(
        x=678.0,
        y=333.0,
        width=226.0,
        height=14.0
    )

    entry_image_15 = PhotoImage(
        file=relative_to_assets("entry_15.png"))
    entry_bg_15 = canvas.create_image(
        791.0,
        360.0,
        image=entry_image_15
    )
    entry_15 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_15.place(
        x=678.0,
        y=352.0,
        width=226.0,
        height=14.0
    )

    entry_image_16 = PhotoImage(
        file=relative_to_assets("entry_16.png"))
    entry_bg_16 = canvas.create_image(
        791.0,
        379.0,
        image=entry_image_16
    )
    entry_16 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_16.place(
        x=678.0,
        y=371.0,
        width=226.0,
        height=14.0
    )

    canvas.create_rectangle(
        677.5,
        326.5000228881836,
        904.0,
        327.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        345.5000228881836,
        904.0,
        346.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        364.5000228881836,
        904.0,
        365.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        383.5000228881836,
        904.0,
        384.038818359375,
        fill="#000000",
        outline="")

    entry_image_17 = PhotoImage(
        file=relative_to_assets("entry_17.png"))
    entry_bg_17 = canvas.create_image(
        791.0,
        414.0,
        image=entry_image_17
    )
    entry_17 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_17.place(
        x=678.0,
        y=406.0,
        width=226.0,
        height=14.0
    )

    entry_image_18 = PhotoImage(
        file=relative_to_assets("entry_18.png"))
    entry_bg_18 = canvas.create_image(
        791.0,
        433.0,
        image=entry_image_18
    )
    entry_18 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_18.place(
        x=678.0,
        y=425.0,
        width=226.0,
        height=14.0
    )

    entry_image_19 = PhotoImage(
        file=relative_to_assets("entry_19.png"))
    entry_bg_19 = canvas.create_image(
        791.0,
        452.0,
        image=entry_image_19
    )
    entry_19 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_19.place(
        x=678.0,
        y=444.0,
        width=226.0,
        height=14.0
    )

    entry_image_20 = PhotoImage(
        file=relative_to_assets("entry_20.png"))
    entry_bg_20 = canvas.create_image(
        791.0,
        471.0,
        image=entry_image_20
    )
    entry_20 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_20.place(
        x=678.0,
        y=463.0,
        width=226.0,
        height=14.0
    )

    canvas.create_rectangle(
        677.5,
        418.5000228881836,
        904.0,
        419.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        437.5000228881836,
        904.0,
        438.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        456.5000228881836,
        904.0,
        457.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        475.5000228881836,
        904.0,
        476.038818359375,
        fill="#000000",
        outline="")

    entry_image_21 = PhotoImage(
        file=relative_to_assets("entry_21.png"))
    entry_bg_21 = canvas.create_image(
        791.0,
        508.0,
        image=entry_image_21
    )
    entry_21 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_21.place(
        x=678.0,
        y=500.0,
        width=226.0,
        height=14.0
    )

    entry_image_22 = PhotoImage(
        file=relative_to_assets("entry_22.png"))
    entry_bg_22 = canvas.create_image(
        791.0,
        527.0,
        image=entry_image_22
    )
    entry_22 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_22.place(
        x=678.0,
        y=519.0,
        width=226.0,
        height=14.0
    )

    entry_image_23 = PhotoImage(
        file=relative_to_assets("entry_23.png"))
    entry_bg_23 = canvas.create_image(
        791.0,
        546.0,
        image=entry_image_23
    )
    entry_23 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_23.place(
        x=678.0,
        y=538.0,
        width=226.0,
        height=14.0
    )

    entry_image_24 = PhotoImage(
        file=relative_to_assets("entry_24.png"))
    entry_bg_24 = canvas.create_image(
        791.0,
        565.0,
        image=entry_image_24
    )
    entry_24 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_24.place(
        x=678.0,
        y=557.0,
        width=226.0,
        height=14.0
    )

    canvas.create_rectangle(
        677.5,
        512.5000228881836,
        904.0,
        513.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        531.5000228881836,
        904.0,
        532.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        550.5000228881836,
        904.0,
        551.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        677.5,
        569.5000228881836,
        904.0,
        570.038818359375,
        fill="#000000",
        outline="")

    entry_image_25 = PhotoImage(
        file=relative_to_assets("entry_25.png"))
    entry_bg_25 = canvas.create_image(
        390.0,
        230.0,
        image=entry_image_25
    )
    entry_25 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_25.place(
        x=277.0,
        y=222.0,
        width=226.0,
        height=14.0
    )

    entry_image_26 = PhotoImage(
        file=relative_to_assets("entry_26.png"))
    entry_bg_26 = canvas.create_image(
        390.0,
        249.0,
        image=entry_image_26
    )
    entry_26 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_26.place(
        x=277.0,
        y=241.0,
        width=226.0,
        height=14.0
    )

    entry_image_27 = PhotoImage(
        file=relative_to_assets("entry_27.png"))
    entry_bg_27 = canvas.create_image(
        390.0,
        268.0,
        image=entry_image_27
    )
    entry_27 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_27.place(
        x=277.0,
        y=260.0,
        width=226.0,
        height=14.0
    )

    entry_image_28 = PhotoImage(
        file=relative_to_assets("entry_28.png"))
    entry_bg_28 = canvas.create_image(
        390.0,
        287.0,
        image=entry_image_28
    )
    entry_28 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_28.place(
        x=277.0,
        y=279.0,
        width=226.0,
        height=14.0
    )

    canvas.create_rectangle(
        276.5,
        234.5000228881836,
        503.0,
        235.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        253.5000228881836,
        503.0,
        254.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        272.5000228881836,
        503.0,
        273.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        291.5000228881836,
        503.0,
        292.038818359375,
        fill="#000000",
        outline="")

    entry_image_29 = PhotoImage(
        file=relative_to_assets("entry_29.png"))
    entry_bg_29 = canvas.create_image(
        390.0,
        323.0,
        image=entry_image_29
    )
    entry_29 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_29.place(
        x=277.0,
        y=315.0,
        width=226.0,
        height=14.0
    )

    entry_image_30 = PhotoImage(
        file=relative_to_assets("entry_30.png"))
    entry_bg_30 = canvas.create_image(
        390.0,
        342.0,
        image=entry_image_30
    )
    entry_30 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_30.place(
        x=277.0,
        y=334.0,
        width=226.0,
        height=14.0
    )

    entry_image_31 = PhotoImage(
        file=relative_to_assets("entry_31.png"))
    entry_bg_31 = canvas.create_image(
        390.0,
        361.0,
        image=entry_image_31
    )
    entry_31 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_31.place(
        x=277.0,
        y=353.0,
        width=226.0,
        height=14.0
    )

    entry_image_32 = PhotoImage(
        file=relative_to_assets("entry_32.png"))
    entry_bg_32 = canvas.create_image(
        390.0,
        380.0,
        image=entry_image_32
    )
    entry_32 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_32.place(
        x=277.0,
        y=372.0,
        width=226.0,
        height=14.0
    )

    canvas.create_rectangle(
        276.5,
        327.5000228881836,
        503.0,
        328.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        346.5000228881836,
        503.0,
        347.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        365.5000228881836,
        503.0,
        366.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        384.5000228881836,
        503.0,
        385.038818359375,
        fill="#000000",
        outline="")

    entry_image_33 = PhotoImage(
        file=relative_to_assets("entry_33.png"))
    entry_bg_33 = canvas.create_image(
        390.0,
        415.0,
        image=entry_image_33
    )
    entry_33 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_33.place(
        x=277.0,
        y=407.0,
        width=226.0,
        height=14.0
    )

    entry_image_34 = PhotoImage(
        file=relative_to_assets("entry_34.png"))
    entry_bg_34 = canvas.create_image(
        390.0,
        434.0,
        image=entry_image_34
    )
    entry_34 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_34.place(
        x=277.0,
        y=426.0,
        width=226.0,
        height=14.0
    )

    entry_image_35 = PhotoImage(
        file=relative_to_assets("entry_35.png"))
    entry_bg_35 = canvas.create_image(
        390.0,
        453.0,
        image=entry_image_35
    )
    entry_35 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_35.place(
        x=277.0,
        y=445.0,
        width=226.0,
        height=14.0
    )

    entry_image_36 = PhotoImage(
        file=relative_to_assets("entry_36.png"))
    entry_bg_36 = canvas.create_image(
        390.0,
        472.0,
        image=entry_image_36
    )
    entry_36 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_36.place(
        x=277.0,
        y=464.0,
        width=226.0,
        height=14.0
    )

    canvas.create_rectangle(
        276.5,
        419.5000228881836,
        503.0,
        420.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        438.5000228881836,
        503.0,
        439.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        457.5000228881836,
        503.0,
        458.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        476.5000228881836,
        503.0,
        477.038818359375,
        fill="#000000",
        outline="")

    entry_image_37 = PhotoImage(
        file=relative_to_assets("entry_37.png"))
    entry_bg_37 = canvas.create_image(
        390.0,
        508.0,
        image=entry_image_37
    )
    entry_37 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_37.place(
        x=277.0,
        y=500.0,
        width=226.0,
        height=14.0
    )

    entry_image_38 = PhotoImage(
        file=relative_to_assets("entry_38.png"))
    entry_bg_38 = canvas.create_image(
        390.0,
        527.0,
        image=entry_image_38
    )
    entry_38 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_38.place(
        x=277.0,
        y=519.0,
        width=226.0,
        height=14.0
    )

    entry_image_39 = PhotoImage(
        file=relative_to_assets("entry_39.png"))
    entry_bg_39 = canvas.create_image(
        390.0,
        546.0,
        image=entry_image_39
    )
    entry_39 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_39.place(
        x=277.0,
        y=538.0,
        width=226.0,
        height=14.0
    )

    entry_image_40 = PhotoImage(
        file=relative_to_assets("entry_40.png"))
    entry_bg_40 = canvas.create_image(
        390.0,
        565.0,
        image=entry_image_40
    )
    entry_40 = Entry(
        bd=0,
        bg="#DAD4BF",
        fg="#000716",
        highlightthickness=0
    )
    entry_40.place(
        x=277.0,
        y=557.0,
        width=226.0,
        height=14.0
    )

    canvas.create_rectangle(
        276.5,
        512.5000228881836,
        503.0,
        513.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        531.5000228881836,
        503.0,
        532.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        550.5000228881836,
        503.0,
        551.038818359375,
        fill="#000000",
        outline="")

    canvas.create_rectangle(
        276.5,
        569.5000228881836,
        503.0,
        570.038818359375,
        fill="#000000",
        outline="")
    window.resizable(False, False)
    window.mainloop()
