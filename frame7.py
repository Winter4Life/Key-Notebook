
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import re

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame7"

def validate_password(password):
    pattern = r"^(?=.*[0-9])(?=.*[!@#$%^&*(),.?\":{}|<>]).*$"
    return re.match(pattern, password)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def read_current_user():
    with open("current_user.txt", "r") as file:
        lines = file.readlines()
        if len(lines) >= 2:
            return lines[0].strip(), lines[1].strip()
        else:
            return None, None

def change_password(current_username, current_password, new_password):
    # Read the accounts file
    with open("accounts.txt", "r") as file:
        accounts = file.readlines()

    # Find the user
    user_index = -1
    for i, line in enumerate(accounts):
        if line.strip() == current_username:
            if accounts[i + 1].strip() == current_password:
                user_index = i
                break

    if user_index == -1:
        messagebox.showerror("Error", "Incorrect password")
        return False

    # Update the password in the accounts file
    accounts[user_index + 1] = new_password + "\n"

    # Save the changes back to the accounts file
    with open("accounts.txt", "w") as file:
        file.writelines(accounts)
    with open("current_user.txt", "r") as file:
        lines = file.readlines()

    # Update the current user's password
    lines[1] = new_password + "\n"

    # Save the changes back to the current_user.txt file
    with open("current_user.txt", "w") as file:
        file.writelines(lines)

    print("Password changed successfully.")
    return True

def back() :
        from frame5 import open_frame5
        window.destroy()
        open_frame5()

def open_frame7():

    with open("current_user.txt", 'r') as file:
        current_username = file.readline().strip()

    def on_change_password():
        # Retrieve values from entry fields
        from frame4 import open_frame4
        current_pass = frame7_currPass.get()
        new_pass = frame7_newPass.get()
        confirm_pass = frame7_confirmPass.get()

        # Check if new password matches confirm password
        if new_pass != confirm_pass:
            messagebox.showerror("Error", "Passwords do not match")
            return
        if not validate_password(new_pass):
            messagebox.showinfo("Error", "Password must contain at least 1 number and special character")
            return

        # Change the password
        if change_password(current_username, current_pass, new_pass):
            # Clear entry fields after successful password change
            frame7_currPass.delete(0, 'end')
            frame7_newPass.delete(0, 'end')
            frame7_confirmPass.delete(0, 'end')
            messagebox.showinfo("Success", "Password changed successfully.")

            window.destroy()
            open_frame4()

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
        465.5,
        image=entry_image_1
    )
    frame7_confirmPass = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Andada Pro", 12),
        show="*"
    )
    frame7_confirmPass.place(
        x=406.0,
        y=432.5,
        width=257.0,
        height=61.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        534.5,
        358.5,
        image=entry_image_2
    )
    frame7_newPass = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Andada Pro", 12),
        show="*"
    )
    frame7_newPass.place(
        x=406.0,
        y=325.5,
        width=257.0,
        height=61.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        534.5,
        257.0,
        image=entry_image_3
    )
    frame7_currPass = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Andada Pro", 12),
    )
    frame7_currPass.place(
        x=406.0,
        y=223.5,
        width=257.0,
        height=61.0
    )

    canvas.create_text(
        395.0,
        130.0,
        anchor="nw",
        text="Change Password",
        fill="#000000",
        font=("RobotoSerifNormalRoman Regular", 36 * -1)
    )

    canvas.create_text(
        410.0,
        207.0,
        anchor="nw",
        text="enter current password",
        fill="#000000",
        font=("AndadaProRoman Regular", 13 * -1)
    )

    canvas.create_text(
        410.0,
        308.0,
        anchor="nw",
        text="new password",
        fill="#000000",
        font=("AndadaProRoman Regular", 13 * -1)
    )

    canvas.create_text(
        410.0,
        415.0,
        anchor="nw",
        text="confirm password",
        fill="#000000",
        font=("AndadaProRoman Regular", 13 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=on_change_password,
        relief="flat"
    )
    button_1.place(
        x=413.0,
        y=536.0,
        width=244.0,
        height=67.0
    )
    button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
    frame7_back_button = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back(),
        relief="flat"
    )
    frame7_back_button.place(
        x=16.0,
        y=584.0,
        width=42.0,
        height=42.0
    )
    window.resizable(False, False)
    window.mainloop()