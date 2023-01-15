from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from tkinter import filedialog
import os 

#-----Arranque da aplicação ------#
class Application:
    def __init__(self, master=None):
        pass


windowNewGame = Tk()

Application(windowNewGame)

"""
ficheiroJogos = "files/games.txt"

def guardarJogo(nameGame, nameCategory, filename):
    fileJogos = open(ficheiroJogos, 'w')
    global jogo, categoria
    jogo = nameGame.get()

"""

def selecionaImgJogo():
    global filename
    filename = filedialog.askopenfilename(title = 'select file', initialdir = "images",  filetypes = (("png files","*.png"),("gif files", "*.gif"), ("all files","*.*")))

    global imgJogo
    global imgJogoid
    imgJogo = PhotoImage(file = filename)

    global canvasJogo
    canvasJogo.itemconfig(imgJogo, imgJogoid)
  
screenWidth = windowNewGame.winfo_screenwidth()
screenHeight = windowNewGame.winfo_screenheight()

appWidth = 1200
appHeight = 600

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
windowNewGame.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

windowNewGame.title('myGameList')
windowNewGame.resizable(0,0)
windowNewGame.iconbitmap('images/video-game-play-pad-boy-gameboy-nintendo_108539.ico')
windowNewGame.configure(bg="beige")

lblGame = Label(windowNewGame, text = 'Name of the Game', fg = 'black', font = ('Calibri', 35), bg = 'white')
lblCategory = Label(windowNewGame, text = 'Category', fg = 'black', font = ('Calibri', 35), bg = 'white')

#Button Selecionar Foto
buttonGamePic = Button(windowNewGame, text = 'Game Image', font=('Helvetica', 20), width = 25, bg = 'pink', command=selecionaImgJogo)
buttonGamePic.place(x = 100, y = 400)


lblGame.place(x = 100, y = 100)
lblCategory.place(x = 100, y = 240)


nameGame = StringVar()
txtGame = Entry(windowNewGame, textvariable=nameGame, width=30, font = ('Calibri', 20))
nameCategory = StringVar()
txtCategory = Entry(windowNewGame, textvariable=nameCategory, width=30, font = ('Calibri', 20))

txtGame.place(x= 500, y =120)
txtCategory.place(x=500, y= 260)

#Button save changes

buttonGuardar = Button(windowNewGame, text = 'SAVE CHANGES', font = ('Helvetica', 15), width = 15, bg = 'pink', command =  'noaction')#lambda: guardarJogo(nameGame, nameCategory, filename))
buttonGuardar.place(x = 850, y =500)


windowNewGame.mainloop()