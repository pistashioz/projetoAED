from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from tkinter import filedialog


#-----Arranque da aplicação ------#
class Application:
    def __init__(self, master=None):
        pass


windowNewGame = Tk()

Application(windowNewGame)





def NovoJogo():
    dc

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

lblGame.place(x = 100, y = 100)
lblCategory.place(x = 100, y = 240)
buttonGamePic.place(x = 100, y = 400)



global canvas_jogo
canvas_jogo = Canvas(windowNewGame, width = 50, height = 50, bd = 4, relief = "sunken")
canvas_jogo.place(x=270, y=70)
global img_jogo, filename
img_jogo = PhotoImage(file = filename)
global image_jogo_id
image_jogo_id = canvas_jogo.create_image(25, 25, image=img_jogo)


btn_guardar = Button(panelConfig, text = "Guardar configurações", height = 3, width=42, 
                command = lambda: [guardarPerfil(continente, filename),  atualizaImgPerfil()])
btn_guardar.place(x=100, y=320)


nameGame = StringVar()
txtGame = Entry(windowNewGame, textvariable=nameGame, width=30, font = ('Calibri', 20))
nameCategory = StringVar()
txtCategory = Entry(windowNewGame, textvariable=nameCategory, width=30, font = ('Calibri', 20))

txtGame.place(x= 500, y =120)
txtCategory.place(x=500, y= 260)

#Button save changes

buttonGuardar = Button(windowNewGame, text = 'SAVE CHANGES', font = ('Helvetica', 15), width = 15, bg = 'pink', command =  lambda: [NovoJogo(nameGame, nameCategory), atualizaImgJogo()])
buttonGuardar.place(x = 850, y =500)


windowNewGame.mainloop()