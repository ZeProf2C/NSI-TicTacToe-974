#!/usr/bin/env python3
from head import *

import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from time import sleep

from Game import *
import iaMinimax

game = Game()
root = tk.Tk()
font = tkFont.Font(size=60)

buttons = [
    [],
    [],
    []
]

def disableButtons():
    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            buttons[i][j].config(state='disabled')
            buttons[i][j].pack()
    root.update()


def win():
    disableButtons()
    messagebox.showinfo("Game Over", "Le joueur %s a gagné !" %(game.winner().upper()))

def NoWinner():
    disableButtons()
    messagebox.showerror("Game Over", "Vous êtes MAUVAIS !")

def iaMove():
    i, j = iaMinimax.minimax(game.get_board(), game.current_player, game.wait_player)
    print(i, j)
    game.move(i, j)
    buttonUpdate(i, j)
    if game.is_there_winner():
        win()
    if game.no_winner():
        NoWinner()
    

def buttonPress(i, j):
    game.move(i, j)
    buttonUpdate(i, j)
    iaMove()
    if game.is_there_winner():
        win()
    if game.no_winner():
        NoWinner()

def buttonUpdate(i, j):
    text = game.get_board(i, j).upper()
    buttons[i][j].config(text=text, state='disabled')
    buttons[i][j].pack()
    root.update()

def initBoard():
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
                    text=game.get_board(i, j).upper(),
                    command=lambda locI=i, locJ=j: buttonPress(locI, locJ),
                    width=3,
                    state='active'
                )
            )
            buttons[i][j].pack(expand=1)

initBoard()
root.mainloop()
