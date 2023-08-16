import tkinter as tk
import ttkbootstrap as ttk

Window = ttk.Window(themename="darkly")
Window.title("calculator")
Window.geometry("400x500")

frame_row0 = ttk.Frame()
frame_row1 = ttk.Frame()
frame_row2 = ttk.Frame()
frame_row3 = ttk.Frame()
frame_row4 = ttk.Frame()

entry=ttk.Entry(Window,width=17,font="calibre 30")
entry.pack(pady=10,)

button = ttk.Button(frame_row0, text="7", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row0, text="8", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row0, text="9", width=15)
button.pack(side="left", padx=5, pady=5)
frame_row0.pack(side="top", anchor="n")

button = ttk.Button(frame_row1, text="4", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row1, text="5", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row1, text="6", width=15)
button.pack(side="left", padx=5, pady=5)
frame_row1.pack(side="top", anchor="n")

button = ttk.Button(frame_row2, text="1", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row2, text="2", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row2, text="3", width=15)
button.pack(side="left", padx=5, pady=5)
frame_row2.pack(side="top", anchor="n")

button = ttk.Button(frame_row3, text="0", width=15)
button.pack(side="left", padx=5, pady=5)
frame_row3.pack(side="top", anchor="n")

button = ttk.Button(frame_row4, text="-", width=10)
button.pack(side="left", padx=4, pady=5)

button = ttk.Button(frame_row4, text="×", width=10)
button.pack(side="left", padx=4, pady=5)

button = ttk.Button(frame_row4, text="+", width=10)
button.pack(side="left", padx=4, pady=5)

button = ttk.Button(frame_row4, text="÷", width=10)
button.pack(side="left", padx=4, pady=5)
frame_row4.pack(side="top", anchor="n")

Window.mainloop()
