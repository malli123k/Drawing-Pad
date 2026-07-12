# 🎨 Drawing Pad

A simple freehand drawing application built with Python and Tkinter. No external libraries required.

---

## Features

- **Pen Tool** — Draw smooth freehand lines on the canvas
- **Eraser Tool** — Erase parts of your drawing
- **Color Picker** — Open a full color chooser dialog to pick any color
- **Preset Colors** — 7 quick-access color buttons for common colors
- **Brush Size Slider** — Adjust brush size from 1 to 20
- **Clear Button** — Wipe the entire canvas and start fresh

---

## Requirements

- Python 3.x
- Tkinter (built into Python on Windows and macOS)

**Linux users** — install Tkinter if missing:

```bash
sudo apt install python3-tk
```

---

## How to Run

```bash
python3 drawing_pad.py
```

---

## Project Structure

```
drawing_pad/
└── drawing_pad.py    # Main application file
```

---

## How to Use

| Action | How |
|---|---|
| Draw | Hold left mouse button and drag |
| Stop drawing | Release left mouse button |
| Switch to eraser | Click the **Eraser** button |
| Switch back to pen | Click any color or **Pen** button |
| Pick a custom color | Click **Color** button |
| Quick color | Click any colored dot on the right |
| Change brush size | Drag the **Size** slider |
| Clear everything | Click **Clear** |

---

## Controls Overview

```
[ ✏ Pen ] [ ⬜ Eraser ] [ 🎨 Color ] [ Size ──●── ] .............. [ 🟥🟡🟢🔵 ] [ 🗑 Clear ]
```

---

## License

Free to use and modify for personal or educational purposes
