import tkinter as tk
import ttkbootstrap as ttk


def math(oper, x, y):
    match oper:
        case "+":
            return x + y

        case "-":
            return x - y

        case "×":
            return x * y

        case "÷":
            return x / y

        case "%":
            return x % y

        case "**":
            return x ** y

        case "//":
            return x // y


operators = ['+', '-', '×', '÷', '%', '**', '//']
num1 = 0
oper = "+"
num2 = 0


def sliceInput(uInput, x, pos, isDouble):
    global num1
    global oper
    global num2
    num1 = uInput[0:pos]
    if isDouble:
        num2 = uInput[pos + 2:]
    else:
        num2 = uInput[pos + 1:]
    oper = x


def checkForDouble(uInput, x, pos):
    nextOperPos = uInput.find(x, pos + 1)
    if nextOperPos != -1:
        return True
    else:
        return False


def findOperator(uInput):
    for x in operators:
        double = False
        pos = uInput.find(x)
        if pos != -1:
            if x == '*' or x == '/':
                if checkForDouble(uInput, x, pos):
                    double = True
                    if x == '*':
                        x = '**'
                    else:
                        x = '//'
            return x, pos, double
    print("none was found")


def proccesInput(uInput):
    x, pos, double = findOperator(uInput)
    sliceInput(uInput, x, pos, double)
    input.set(math(oper, int(num1), int(num2)))


def buttonInput(num):
    current_input = input.get()
    current_input += str(num)
    input.set(current_input)

# window
Window = ttk.Window(themename="darkly")
Window.title("calculator")

# tk var
input = tk.StringVar()

# widgets
frame_row0 = ttk.Frame()
frame_row1 = ttk.Frame()
frame_row2 = ttk.Frame()
frame_row3 = ttk.Frame()
frame_row4 = ttk.Frame()

entry=ttk.Entry(Window,width=17,font="calibre 30", textvariable=input)
entry.pack(pady=10)

button = ttk.Button(frame_row0, text="7", width=15, command=lambda: buttonInput(7))
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row0, text="8", width=15, command=lambda: buttonInput(8))
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row0, text="9", width=15, command=lambda: buttonInput(9))
button.pack(side="left", padx=5, pady=5)
frame_row0.pack(side="top", anchor="n")

button = ttk.Button(frame_row1, text="4", width=15, command=lambda: buttonInput(4))
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row1, text="5", width=15, command=lambda: buttonInput(5))
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row1, text="6", width=15, command=lambda: buttonInput(6))
button.pack(side="left", padx=5, pady=5)
frame_row1.pack(side="top", anchor="n")

button = ttk.Button(frame_row2, text="1", width=15, command=lambda: buttonInput(1))
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row2, text="2", width=15, command=lambda: buttonInput(2))
button.pack(side="left", padx=5, pady=5)

button = ttk.Button(frame_row2, text="3", width=15, command=lambda: buttonInput(3))
button.pack(side="left", padx=5, pady=5)
frame_row2.pack(side="top", anchor="n")

button = ttk.Button(frame_row3, text="0", width=15, command=lambda: buttonInput(0))
button.pack(side="left", padx=5, pady=5)
frame_row3.pack(side="top", anchor="n")

button = ttk.Button(frame_row4, text="-", width=10, command=lambda: buttonInput("-"))
button.pack(side="left", padx=4, pady=5)

button = ttk.Button(frame_row4, text="×", width=10, command=lambda: buttonInput("×"))
button.pack(side="left", padx=4, pady=5)

button = ttk.Button(frame_row4, text="+", width=10, command=lambda: buttonInput("+"))
button.pack(side="left", padx=4, pady=5)

button = ttk.Button(frame_row4, text="÷", width=10, command=lambda: buttonInput("÷"))
button.pack(side="left", padx=4, pady=5)
frame_row4.pack(side="top", anchor="n")

Window.mainloop()
