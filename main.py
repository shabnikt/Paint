from tkinter import *
from tkinter.colorchooser import *

import setup as s
from image_file import load_image
 
brush_size = s.BRUSH_SIZE
color = s.DEFAULT_COLOR
l_x1 = 0
l_y1 = 0
shape_state = 'line'


window = Tk()
window.title('Paint')
canvas = Canvas(width=s.WIDTH, height=s.HEIGHT, bg=s.BG_COLOR)


# Drawing funcs
def draw(_event):
    x1 = _event.x - brush_size
    y1 = _event.y - brush_size
    x2 = _event.x + brush_size
    y2 = _event.y + brush_size
    canvas.create_oval(x1, y1,
                       x2, y2,
                       fill=color,
                       outline=color)


def active_paint(_event):
    canvas.bind('<B1-Motion>', draw)
    canvas.bind('<ButtonPress-1>', draw)
        

canvas.bind('<1>', active_paint)


# Drawing shapes funcs
def change_fp(_event):
    global l_x1, l_y1
    l_x1, l_y1 = _event.x, _event.y # l_x1 = _event.x и l_y1 = _event.y
    

def draw_shape(_event):
    l_x2, l_y2 = _event.x, _event.y
    if shape_state == 'line':
        canvas.create_line(l_x1, l_y1,
                           l_x2, l_y2,
                           fill=color, width=brush_size//5)
    elif shape_state == 'square':
        canvas.create_rectangle(l_x1, l_y1,
                           l_x2, l_y2,
                           fill=color, width=brush_size//5)
    elif shape_state == 'oval':
        canvas.create_oval(l_x1, l_y1,
                           l_x2, l_y2,
                           fill=color, width=brush_size//5)


canvas.bind('<3>', change_fp)
canvas.bind('<ButtonRelease-3>', draw_shape)


def change_color(cvet):
    global color
    color = cvet
    if cvet == s.DEFAULT_COLOR:
        br_btn.config(bg='light grey')
        er_btn.config(bg='white')
    elif cvet == s.BG_COLOR:
        er_btn.config(bg='light grey')
        br_btn.config(bg='white')
    

def change_brush_size(event):
    global brush_size
    brush_size = slider.get()


def change_shape_state(state):
    global shape_state
    shape_state = state


br_icon = load_image('brush.png')
er_icon = load_image('eraser.png')
line_icon = load_image('line.png')
square_icon = load_image('square.png')
oval_icon = load_image('oval.png')


br_btn = Button(image=br_icon, command=lambda: change_color(s.DEFAULT_COLOR))
er_btn = Button(image=er_icon, command=lambda: change_color(s.BG_COLOR))
del_all_btn = Button(text='Remove all', command=lambda: canvas.delete('all'))

slider = Scale(from_=5, to=30, orient=HORIZONTAL, length=100,
               command=change_brush_size)
slider.set(s.BRUSH_SIZE)

line_btn = Button(image=line_icon, command=lambda: change_shape_state('line'))
square_btn = Button(image=square_icon, command=lambda: change_shape_state('square'))
oval_btn = Button(image=oval_icon, command=lambda: change_shape_state('oval'))

slider.grid(row=1, column=3, columnspan=4)
br_btn.grid(row=1, column=7)
er_btn.grid(row=1, column=8)
del_all_btn.grid(row=1, column=9)

line_btn.grid(row=1, column=10)
square_btn.grid(row=1, column=11)
oval_btn.grid(row=1, column=12)


canvas.grid(row=2,
            column=3,
            rowspan=50,
            columnspan=50,
            padx=5,
            pady=5)


# Change color sidebar
def create_color_btn(_color, _row, _column):
    btn = Button(width=2, height=1, bg=_color,
                 command=lambda : change_color(_color))
    btn.grid(row=_row, column=_column, padx=2)


def get_color():
    global color
    color = askcolor(title='Color Picker')[1]


colors = [['#2acaea', '#FFD700', '#FF0000'],
          ['#5ac18e', '#f7347a', '#ffa500'],
          ['#ac25e2', '#101010', '#ffffff']]

rows = len(colors) # 3
columns = len(colors[0]) # 3

for i in range(rows):
    for j in range(columns):
        btn_color = colors[i][j]
        create_color_btn(btn_color, i + 2, j)
    

picker_btn = Button(text='Color Picker', width=10,
                    command=get_color)
picker_btn.grid(row=i+3, columnspan=3)

window.mainloop()
