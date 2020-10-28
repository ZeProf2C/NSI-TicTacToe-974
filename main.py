#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import pyautogui

from time import sleep

from Game import *

game = Game()
root = tk.Tk()
font = tkFont.Font(size=60)

buttons = [
    [],
    [],
    []
]

def win():
    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            buttons[i][j].config(state='disabled')

def buttonPress(i, j):
    print("click %s %s" %(i, j))
    game.move(i, j)
    buttonUpdate(i, j)

    if game.is_there_winner():
        win()

def buttonUpdate(i, j):
    text = game.getBoard(i, j).upper()
    buttons[i][j].config(text=text)

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=root,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        buttons[i].append(
            tk.Button(
                master=frame,
                font=font,
                text=game.getBoard(i, j).upper(),
                command=lambda locI=i, locJ=j: buttonPress(locI, locJ),
                width=3
            )
        )
        buttons[i][j].pack(expand=1)
root.mainloop()
