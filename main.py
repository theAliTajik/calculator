import tkinter as tk
import ttkbootstrap as ttk

Window = ttk.Window(themename="darkly")
Window.title("calculator")
Window.geometry("500x300")

frame_row0 = ttk.Frame()
frame_row1 = ttk.Frame()
frame_row2 = ttk.Frame()
frame_row3 = ttk.Frame()
frame_row4 = ttk.Frame()
frame_delete = ttk.Frame()

invincible = tk.StringVar()

entry=ttk.Entry(Window,width=19,font="calibre 33")
entry.pack(pady=10)

button = ttk.Button(frame_delete, text="CE", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_delete, text="C", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_delete, text="Delete", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_delete, text="÷", width=5)
button.pack(side="left", padx=5, pady=5)
frame_delete.pack(side="top", anchor="n")

button = ttk.Button(frame_row0, text="7", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row0, text="8", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row0, text="9", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row0, text="×", width=5)
button.pack(side="left", padx=5, pady=5)
frame_row0.pack(side="top", anchor="n")

button = ttk.Button(frame_row1, text="4", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row1, text="5", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row1, text="6", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row1, text="-", width=5)
button.pack(side="left", padx=5, pady=5)
frame_row1.pack(side="top", anchor="n")

button = ttk.Button(frame_row2, text="1", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row2, text="2", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row2, text="3", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row2, text="+", width=5)
button.pack(side="left", padx=5, pady=5)
frame_row2.pack(side="top", anchor="n")

invic = ttk.Label(frame_row3,text="",width=18)
invic.pack(side="left", padx=6, pady=3)

button = ttk.Button(frame_row3, text="0", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row3, text=".", width=15)
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row3, text="=", width=5)
button.pack(side="left", padx=5, pady=5)
frame_row3.pack(side="top", anchor="n")



Window.mainloop()
