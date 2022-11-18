import pyglet, tkinter
pyglet.font.add_file("Pixeltype.ttf")
from tkinter import *
from tkinter import ttk, font
from pygame import mixer
import time

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


mixer.init()
mixer.music.load('music.wav')
mixer.music.set_volume(0.1)
mixer.music.play(loops= -1)

win = Tk(className=" ")
win.configure(bg='black')

win.geometry("600x460")

canvas1 = Canvas(win, width= 600, height= 460, bg='black')
entry1 = tkinter.Entry(win, justify=CENTER, font=('Pixeltype 20'), bg='black', fg='gray')
canvas1.create_window(300, 140, window=entry1,)

variable1 = StringVar(win)
variable1.set('in')

variable2 = StringVar(win)
variable2.set('ft')

options1 = ['in','ft','yd','mi','cm','m','km','g','kg','oz','lbs','F','C',"K"]
options2 = ['in','ft','yd','mi','cm','m','km','g','kg','oz','lbs','F','C',"K"]
options_menu1 = OptionMenu(win, variable1, *options1)
options_menu2 = OptionMenu(win, variable2, *options2)
options_menu1.configure(font=('Pixeltype 20'), bg='black', fg='gray')
options_menu2.configure(font=('Pixeltype 20'), bg='black', fg='gray')

canvas1.create_text(300, 200, text="TO", fill="gray", font=('Pixeltype 15 bold'))

canvas1.create_window(230,200, window=options_menu1)
canvas1.create_window(370,200, window=options_menu2)

canvas1.create_text(300, 50, text="TI UNIT CONVERTER 3000", fill="gray", font=('Pixeltype 20 bold'))
label2 = tkinter.Label(win, text="YOU'VE GOT THIS!", fg="gray", font=('Pixeltype 20 bold'), bg='black')

canvas1.create_window(300, 400, window=label2)
canvas1.pack()

def convert():
    x1 = entry1.get()
    x2 = variable1.get()
    x3 = variable2.get()

    if x2 == 'in':
        if x3 == 'in':
            result = float(x1)
        elif x3 == 'ft':
            result = float(x1)/12
        elif x3 == 'yd':
            result = float(x1)/12/3
        elif x3 == 'mi':
            result = float(x1)/63360
        elif x3 == 'cm':
            result = float(x1)*2.54
        elif x3 == 'm':
            result = float(x1)*0.0254
        elif x3 == 'km':
            result = float(x1)*0.0000254
        else:
            result = 'Error'

    elif x2 == 'ft':
        if x3 == 'in':
            result = float(x1)*12
        elif x3 == 'ft':
            result = float(x1)/12*12
        elif x3 == 'yd':
            result = float(x1)/12/3*12
        elif x3 == 'mi':
            result = float(x1)/63360*12
        elif x3 == 'cm':
            result = float(x1)*2.54*12
        elif x3 == 'm':
            result = float(x1)*0.0254*12
        elif x3 == 'km':
            result = float(x1)*0.0000254*12
        else:
            result = 'Error'

    elif x2 == 'mi':
        if x3 == 'in':
            result = float(x1)*12*3*1760
        elif x3 == 'ft':
            result = float(x1)/12*12*3*1760
        elif x3 == 'yd':
            result = float(x1)/12/3*12*3*1760
        elif x3 == 'mi':
            result = float(x1)/63360*12*3*1760
        elif x3 == 'cm':
            result = float(x1)*2.54*12*3*1760
        elif x3 == 'm':
            result = float(x1)*0.0254*12*3*1760
        elif x3 == 'km':
            result = float(x1)*0.0000254*12*3*1760
        else:
            result = 'Error'

    elif x2 == 'yd':
        if x3 == 'in':
            result = float(x1)*12*3
        elif x3 == 'ft':
            result = float(x1)/12*12*3
        elif x3 == 'yd':
            result = float(x1)/12/3*12*3
        elif x3 == 'mi':
            result = float(x1)/63360*12*3
        elif x3 == 'cm':
            result = float(x1)*2.54*12*3
        elif x3 == 'm':
            result = float(x1)*0.0254*12*3
        elif x3 == 'km':
            result = float(x1)*0.0000254*12*3
        else:
            result = 'Error'

    elif x2 == 'cm':
        if x3 == 'in':
            result = float(x1)/2.54
        elif x3 == 'ft':
            result = float(x1)/2.54/12
        elif x3 == 'yd':
            result = float(x1)/2.54/12/3
        elif x3 == 'mi':
            result = float(x1)/2.54/63360
        elif x3 == 'cm':
            result = float(x1)
        elif x3 == 'm':
            result = float(x1)/100
        elif x3 == 'km':
            result = float(x1)/100/1000
        else:
            result = 'Error'

    elif x2 == 'm':
        if x3 == 'in':
            result = float(x1)/2.54*100
        elif x3 == 'ft':
            result = float(x1)/2.54/12*100
        elif x3 == 'yd':
            result = float(x1)/2.54/12/3*100
        elif x3 == 'mi':
            result = float(x1)/2.54/63360*100
        elif x3 == 'cm':
            result = float(x1)*100
        elif x3 == 'm':
            result = float(x1)/100*100
        elif x3 == 'km':
            result = float(x1)*100*1000
        else:
            result = 'Error'

    elif x2 == 'km':
        if x3 == 'in':
            result = float(x1) / 2.54 * 100*1000
        elif x3 == 'ft':
            result = float(x1) / 2.54 / 12 * 100*1000
        elif x3 == 'yd':
            result = float(x1) / 2.54 / 12 / 3 * 100*1000
        elif x3 == 'mi':
            result = float(x1) / 2.54 / 63360 * 100*1000
        elif x3 == 'cm':
            result = float(x1) * 100*1000
        elif x3 == 'm':
            result = float(x1) / 100 * 100*1000
        elif x3 == 'km':
            result = float(x1) * 100 * 1000*1000
        else:
            result = 'Error'

    elif x2 == 'g':
        if x3 == 'g':
            result = float(x1)
        elif x3 == 'kg':
            result = float(x1)/1000
        elif x3 == 'oz':
            result = float(x1)*0.035274
        elif x3 == 'lbs':
            result = float(x1)*0.00220462
        else:
            result = 'Error'

    elif x2 == 'kg':
        if x3 == 'g':
            result = float(x1)*1000
        elif x3 == 'kg':
            result = float(x1)/1000*1000
        elif x3 == 'oz':
            result = float(x1)*0.035274*1000
        elif x3 == 'lbs':
            result = float(x1)*0.00220462*1000
        else:
            result = 'Error'

    elif x2 == 'oz':
        if x3 == 'g':
            result = float(x1)*28.3495
        elif x3 == 'kg':
            result = float(x1)*28.3495/1000
        elif x3 == 'oz':
            result = float(x1)
        elif x3 == 'lbs':
            result = float(x1)/16
        else:
            result = 'Error'

    elif x2 == 'lbs':
        if x3 == 'g':
            result = float(x1)*28.3495*16
        elif x3 == 'kg':
            result = float(x1)*28.3495/1000*16
        elif x3 == 'oz':
            result = float(x1)*16
        elif x3 == 'lbs':
            result = float(x1)/16*16
        else:
            result = 'Error'

    elif x2 == 'F':
        if x3 == 'F':
            result = float(x1)
        elif x3 == 'C':
            result = (float(x1)-32)*5/9
        elif x3 == 'K':
            result = (float(x1)-32)*5/9 + 273.15
        else:
            result = 'Error'

    elif x2 == 'C':
        if x3 == 'F':
            result = (float(x1)* 9/5) + 32
        elif x3 == 'C':
            result = float(x1)
        elif x3 == 'K':
            result = float(x1) + 273.15
        else:
            result = 'Error'

    elif x2 == 'K':
        if x3 == 'F':
            result = (float(x1)-273.15)* 9/5 + 32
        elif x3 == 'C':
            result = float(x1) - 273.15
        elif x3 == 'K':
            result = float(x1)
        else:
            result = 'Error'


    if result == 'Error':
        label1 = tkinter.Label(win, text=result, font='Pixeltype 30', bg='black', fg='gray', padx=170)
        canvas1.create_window(300, 330, window=label1)
    else:
        label1 = tkinter.Label(win, text=str(round(result, 7)) + " " + x3, font='Pixeltype 30', bg='black', fg='gray', padx=170)
        canvas1.create_window(300, 330, window=label1)

# win.bind('<Return>')

button1 = tkinter.Button(text='Convert', command=convert, font='Pixeltype 15', bg='black', fg='gray')
canvas1.create_window(300, 280, window=button1)

win.mainloop()

