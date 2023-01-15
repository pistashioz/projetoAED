from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from interfaceConta import logInInterface, signUp
import tkinter as tk
import os
from jogo import *


def atualizaImgJogo():
  """
  atualiza canvas de imagem de jogo no PanelUser (HEADER), com imagem guardada em ficheiro
  """
  global imgJogo
  global imageHeader_id
  imgJogo = PhotoImage(file = filename)
  ctnUser.itemconfig(imageHeader_id, image=imgJogo)




def selecionaPerfil():
  """
  selecionar imagem para o perfil, nas configurações, a partir de FileDialog
  """
  global filename
  filename = filedialog.askopenfilename(title = "Select file", initialdir= "./imagens",
              filetypes = (("png files","*.png"),("gif files", "*.gif"), ("all files","*.*")))
  
  global img_jogo
  global image_jogo_id
  img_jogo = PhotoImage(file = filename)
  # change image on canvas
  global canvas_jogo
  canvas_jogo.itemconfig(image_jogo_id, image=img_jogo)


def PanelConfigurar():
    # ------------------------------------------------------------


    panelJogos = PanedWindow(window, width = 1200, height =600, bd = "3", relief = "sunken")
    panelJogos.place(x=0, y=0)

    btn_selecionar = Button(panelJogos, text = "Selecione imagem \n do jogo", width = 20, height = 5, 
                    command = selecionaPerfil)

    btn_selecionar.place(x=250, y= 210)
    global canvas_jogo
    canvas_jogo = Canvas(panelJogos, width = 180, height = 220)
    canvas_jogo.place(x=70, y=180)
    global img_jogo, filename
    img_jogo = PhotoImage(file = filename)
    global image_jogo_id
    image_jogo_id = canvas_jogo.create_image(25, 25, image=img_jogo)

    lblGame = Label(panelJogos, text = 'Name of the Game', fg = 'black', font = ('Calibri', 12), bg = 'white')
    lblCategory = Label(panelJogos, text = 'Category', fg = 'black', font = ('Calibri', 12), bg = 'white')


    lblGame.place(x = 50, y = 80)
    lblCategory.place(x = 50, y = 120)


    nameGame = StringVar()
    txtGame = Entry(panelJogos, textvariable=nameGame, width=30, font = ('Calibri',10))
    nameCategory = StringVar()
    txtCategory = Entry(panelJogos, textvariable=nameCategory, width=30, font = ('Calibri', 10))

    txtGame.place(x= 180, y =80)
    txtCategory.place(x=180, y= 120)

    #---- GUARDAR configurações
    btn_guardar = Button(panelJogos, text = "Guardar configurações", height = 3, width=24, 
                    command = lambda: [guardarJogo(nameCategory, nameGame, filename),  atualizaImgJogo()])
    btn_guardar.place(x=450, y=320)




#-----Arranque da aplicação ------#
class Application:
    def __init__(self, master=None):
        pass
window = Tk()
windowFechar = window
Application(window)
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 1200
appHeight = 600
x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
window.title('myGameList')
window.resizable(0,0)
window.iconbitmap('images/video-game-play-pad-boy-gameboy-nintendo_108539.ico')
window.configure(bg="beige")
#opcoesBarra
barraMenu = Menu(window, background='orange', fg='white')
barraMenu.add_command(label="LIBRARY", command="noaction")
barraMenu.add_command(label="COMMUNITY", command="noaction")
barraMenu.add_command(label="ADD A GAME", command="noaction")
window.configure(menu=barraMenu)
#FrameCatalogo
frame1 = LabelFrame(window, width=280, height=660, bg='gray35', borderwidth=0, highlightthickness=0)
frame1.place(x=0, y=30)
frameNewGames = LabelFrame(window, width = 920, height=220, relief = "ridge", bg='RoyalBlue4', borderwidth=0, highlightthickness=0)
frameNewGames.place(x=280, y=30)
frame2 = LabelFrame(window, width = 920, height=450, bg='gray45', borderwidth=0, highlightthickness=0)
frame2.place(x=280, y=250)
frame4 = LabelFrame(window,width=280, height=100, bg='gray13', borderwidth=0, highlightthickness=0)
frame4.place(x=0, y=30)
frameLoginBackground = LabelFrame(window,width=1200,height=30, bg="thistle",borderwidth=0, highlightthickness=0)
frameLoginBackground.place(x=0, y=0)
frameLinha1 = LabelFrame(frameNewGames,width=850,height=1, bg="white",borderwidth=0, highlightthickness=0)
frameLinha1.place(x=130, y=20)

# Treeview New Games




# Add the rowheight and vertical scrollbar

s=ttk.Style()



tree = ttk.Treeview(frameNewGames, selectmode='browse', columns = ('Image', 'Name', 'Category'))
treeScroll = Scrollbar(frameNewGames)
treeScroll.pack(side = RIGHT, fill = Y)


tree = ttk.Treeview(frameNewGames, selectmode='browse', columns = ('Image', 'Name', 'Category'), yscrollcommand=treeScroll.set)
tree.place(x=0, y=10)
scrollbary = Scrollbar(tree, orient=VERTICAL)
scrollbary.place()
s.configure('Treeview', rowheight=150, fieldbackground="blue", background="blue", yscrollcommand = scrollbary.set)
s.configure('Treeview', rowheight=150, fieldbackground="blue", background="blue")
tree.column('Image', width =100, anchor = 'center', stretch=False)
tree.column('Name', width = 350, anchor = 'center', stretch=False)
tree.column('Category', width = 350, anchor = 'center', stretch=False)
tree.column('Name', width = 300, anchor = 'center', stretch=False)
tree.column('Category', width = 300, anchor = 'center', stretch=False)

tree.heading('Image', text = 'Image')
tree.heading('Name', text = 'Name')
tree.heading('Category', text = 'Category')


img = tk.PhotoImage(file = 'images/stray.png') #aqui tiene que aparecer el url para la imagen, abrir los archivos
tree.insert('', 'end', image = img, value = ('',jogo, categoria)) #aqui las variables para titulo y el nombre
tree.place(x=0, y=35)

treeScroll.configure(command=tree.yview)
tree.pack()


#Labels

lblWhatsNew = Label(frameNewGames, text = 'NEW GAMES', font=('Helvetica', 12, "bold"), bg="RoyalBlue4", fg="white")
lblWhatsNew.place(x=20, y=10)
lblWhatsNew.place(x=20, y=0)

lblMostViewed = Label(frame2, text = 'MOST VIEWED', font=('Helvetica', 12, "bold"), bg="gray45", fg="white")
lblMostViewed.place(x=20, y=20)
lblMostLiked = Label(frame2, text='MOST LIKED', font=('Helvetica', 12, "bold"), bg="gray45", fg="white")
lblMostLiked.place(x=20, y=150)
lblMyFavorites = Label(frame2, text = 'MY FAVORITES', font=('Helvetica', 12, "bold"), bg="gray45", fg="white")
lblMyFavorites.place(x=20, y=280)
# Search Category
column = ['ALL', 'ACTION-ADVENTURE', 'ACTION', 'ADVENTURE', 'ARCADE', 'CASUAL', 'COZY', 'CRIME', 'CYBERPUNK', 'EXPERIMENTAL', 'FAMILY-FRIENDLY', 'FANTASY', 'FIRST-PERSON', 'HORROR', 'MINIGAMES', 'MISTERY', 'NOSTALGIA', 'RACING', 'RELAXING', 'SCI-FI']
search_by = ttk.Combobox(frame4, values = column, width = 43, height= 100)
search_by.current(0)
search_by.place(x = 0, y = 0)
# Search Text
txtSearch = Entry(frame4, width=46)
txtSearch.place(x=0, y=30)
# Search Button
btnSearch = Button(frame4, text='Search', width=10, height=1, bg="gray13", fg="white")
btnSearch.place(x= 100, y = 60)
# Login Button
btnLogin = Button(window, text="Login",font=('Helvetica', 10), width=6, height=1, bg="orange", fg="black", command= lambda: logInInterface(windowFechar))
btnLogin.place(x = 985, y = 1)
# Create Account Button
btnCreateAccount = Button(window, text="Create Account",font=('Helvetica', 10), width=12, height=1, bg="orange", fg="black", command=signUp)
btnCreateAccount.place(x = 1095, y = 1)
window.mainloop()
