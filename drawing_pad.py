import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Drawing Pad")
root.geometry("900x650")
root.configure(bg="#1a1a2e")

current_color = ["#ffffff"]
brush_size = [4]
last_x = [None]
last_y = [None]
drawing_mode = ["pen"]

canvas = tk.Canvas(root, bg="#0f0f23", cursor="crosshair", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

toolbar = tk.Frame(root, bg="#1a1a2e", height=55)
toolbar.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=(0, 10))
toolbar.pack_propagate(False)

def draw(event):
    if last_x[0] and last_y[0]:
        if drawing_mode[0] == "eraser":
            color = "#0f0f23"
        else:
            color = current_color[0]
        size = brush_size[0] * 3 if drawing_mode[0] == "eraser" else brush_size[0]
        canvas.create_line(last_x[0], last_y[0], event.x, event.y,
                           width=size, fill=color, capstyle=tk.ROUND, smooth=True)
    last_x[0] = event.x
    last_y[0] = event.y

def reset_pos(event):
    last_x[0] = None
    last_y[0] = None

def pick_color():
    color = colorchooser.askcolor(color=current_color[0])[1]
    if color:
        current_color[0] = color
        color_btn.configure(bg=color)
        drawing_mode[0] = "pen"

def set_size(val):
    brush_size[0] = int(val)

def clear_canvas():
    canvas.delete("all")

def set_mode(mode):
    drawing_mode[0] = mode

canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset_pos)

btn_style = {"font": ("Segoe UI", 9, "bold"), "relief": tk.FLAT, "bd": 0,
             "padx": 14, "pady": 8, "cursor": "hand2"}

pen_btn = tk.Button(toolbar, text="✏ Pen", bg="#4a4e8a", fg="white",
                    command=lambda: set_mode("pen"), **btn_style)
pen_btn.pack(side=tk.LEFT, padx=(0, 4))

eraser_btn = tk.Button(toolbar, text="⬜ Eraser", bg="#4a4e8a", fg="white",
                       command=lambda: set_mode("eraser"), **btn_style)
eraser_btn.pack(side=tk.LEFT, padx=4)

color_btn = tk.Button(toolbar, text="🎨 Color", bg=current_color[0], fg="#1a1a2e",
                      command=pick_color, **btn_style)
color_btn.pack(side=tk.LEFT, padx=4)

tk.Label(toolbar, text="Size:", bg="#1a1a2e", fg="#aaaacc",
         font=("Segoe UI", 9)).pack(side=tk.LEFT, padx=(12, 4))

size_slider = tk.Scale(toolbar, from_=1, to=20, orient=tk.HORIZONTAL,
                       command=set_size, bg="#1a1a2e", fg="#aaaacc",
                       troughcolor="#4a4e8a", highlightthickness=0,
                       length=120, sliderlength=16)
size_slider.set(4)
size_slider.pack(side=tk.LEFT, padx=4)

clear_btn = tk.Button(toolbar, text="🗑 Clear", bg="#8a2b4a", fg="white",
                      command=clear_canvas, **btn_style)
clear_btn.pack(side=tk.RIGHT, padx=(4, 0))

preset_colors = ["#ff6b6b", "#ffd93d", "#6bcb77", "#4d96ff", "#ff922b", "#cc5de8", "#ffffff"]
for c in preset_colors:
    dot = tk.Button(toolbar, bg=c, width=2, relief=tk.FLAT, cursor="hand2",
                    command=lambda col=c: [current_color.__setitem__(0, col),
                                           color_btn.configure(bg=col),
                                           set_mode("pen")])
    dot.pack(side=tk.RIGHT, padx=2)

root.mainloop()
