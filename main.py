#!/usr/bin/env python3

import tkinter as tk
import tkinter.font as tkFont
import pyautogui

from Game import *

game = Game()


window = tk.Tk()
font = tkFont.Font(size=60)

def buttonPress(i, j):
    print("click %s %s" %(i, j))
    game.move(i, j)
    button[i][j].config(text = game.getBoard(i, j).upper())

button = [
    [],
    [],
    []
]

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        button[i].append(
            tk.Button(
                master=frame,
                font=font,
                text=game.getBoard(i, j),
                command=lambda locI=i, locJ=j: buttonPress(locI, locJ),
                width=3
            )
        )
        button[i][j].pack(expand=1)

window.mainloop()