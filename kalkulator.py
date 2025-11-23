import tkinter as tk
from tkinter import *

def btn_click(val):
    current = display_var.get()

    if val == "C":
        display_var.set("")

    elif val == "⌫":
        display_var.set(current[:-1])

    elif val == "()":
        open_b = current.count("(")
        close_b = current.count(")")

        if open_b > close_b:
            display_var.set(current + ")")
        else:
            if current != "" and (current[-1].isdigit() or current[-1] == ")"):
                display_var.set(current + "*(")
            else:
                display_var.set(current + "(")

    elif val == "=":
        try:
            result = str(eval(current))
            display_var.set(result)
        except:
            display_var.set("ERROR")

    elif val == "%":
        display_var.set(current + "/100")

    else:
        display_var.set(current + val)



root = tk.Tk()
root.title("Hanif Kalkulator")
root.geometry("380x660")
root.config(bg="#0d0d0d")
root.resizable(False, False)

top_frame = Frame(root, bg="#1a1a1a", height=180)
top_frame.pack(fill="x")

title_label = Label(top_frame, text="Hanif Kalkulator", bg="#1a1a1a", fg="#00d9ff", font=("Arial", 16))
title_label.pack(pady=10)

display_var = StringVar()
display = Label(top_frame, textvariable=display_var, bg="#1a1a1a", fg="white",
                font=("Arial", 38, "bold"), anchor="e", padx=20)
display.pack(fill="both", expand=True)

watermark = Label(top_frame, text="— Hanif Kalkulator —", bg="#1a1a1a", fg="#00d9ff", font=("Arial", 10))
watermark.pack()

btn_frame = Frame(root, bg="#0d0d0d")
btn_frame.pack(pady=10)

btn_texts = [
    ["C", "⌫", "%", "()"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

color_operator = "#ff9f0a"
color_clear = "#ddd9d2"
color_back = "#ddd9d2"
color_percent = "#ddd9d2"
color_bracket = "#ddd9d2"
color_number = "#2b2b2b"

for r, row in enumerate(btn_texts):
    for c, text in enumerate(row):

        if text == "C":
            bg = color_clear; fg = "black"
        elif text == "⌫":
            bg = color_back; fg = "black"
        elif text == "%":
            bg = color_percent; fg = "black"
        elif text == "()":
            bg = color_bracket; fg = "black"
        elif text in ["+", "-", "*", "/", "="]:
            bg = color_operator; fg = "white"
        else:
            bg = color_number; fg = "white"

        btn = Button(btn_frame, text=text, font=("Arial", 18), width=4, height=2, relief="flat",
                     bg=bg, fg=fg, activebackground="#444", activeforeground="white",
                     command=lambda v=text: btn_click(v))

        btn.grid(row=r, column=c, padx=10, pady=10, ipadx=4, ipady=4)

root.mainloop()
