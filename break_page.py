from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
import time

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./home_assets")

def to_main_menu():
    window.destroy()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def break_seven():
    t_now_s = time.localtime()
    e1 = entry_1.get()
    file_object = open('Time_Stamps.txt', 'a')
    file_object.write(f'\n -- A 7 min break has been activated -- AT -- {time.strftime("%H:%M:%S", t_now_s)} --')
    file_object.write(f'\n -- {e1} --')
    entry_1.delete(0, 'end')
    entry_1.insert(0,"*Break Activated*")
                      
def break_two():
    t_now_t = time.localtime()
    e2 = entry_2.get()
    file_object_t = open('Time_Stamps.txt', 'a')
    file_object_t.write(f'\n -- A 20 min break has been activated -- AT -- {time.strftime("%H:%M:%S", t_now_t)} --')
    file_object_t.write(f'\n -- {e2} --')
    entry_2.delete(0, 'end')
    entry_2.insert(0,"*Break Activated*")   
                        
def break_ref():
    t_now_r = time.localtime()
    file_object_r = open('Time_Stamps.txt', 'a')
    file_object_r.write(f'\n -- A 45 min refreshment break has been activated -- AT -- {time.strftime("%H:%M:%S", t_now_r)} --')


window = Tk()

window.geometry("1512x982")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 982,
    width = 1512,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    756.0,
    491.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= to_main_menu,
    relief="flat"
)
button_1.place(
    x=617.5,
    y=805.8970336914062,
    width=301.0,
    height=68.57296752929688
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= break_seven,
    relief="flat"
)
button_2.place(
    x=83.0,
    y=296.0,
    width=121.0,
    height=56.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=break_ref,
    relief="flat"
)
button_3.place(
    x=858.0,
    y=285.0,
    width=286.0,
    height=56.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=break_two,
    relief="flat"
)
button_4.place(
    x=84.0,
    y=364.0,
    width=121.0,
    height=56.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    456.5,
    324.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_1.insert(0,"*specify reason*")
entry_1.place(
    x=253.0,
    y=308.0,
    width=407.0,
    height=31.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    456.5,
    392.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_2.insert(0,"*specify reason*")
entry_2.place(
    x=253.0,
    y=376.0,
    width=407.0,
    height=31.0
)
window.resizable(False, False)
window.mainloop()
