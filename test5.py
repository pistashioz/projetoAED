from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from interfaceConta import *
import tkinter as tk
import os
from jogo2 import *

def switch():
    """
    """

def PerfilConfigurar():
    # ------------------------------------------------------------
    perfilConfig = PanedWindow(window, width = 700, height = 450, bd = "3", relief = "sunken")
    perfilConfig.place(x=0, y=50)

    btn_selecionar = Button(perfilConfig, text = "Selecione imagem \nde perfil", width = 14, height = 3, 
                    command = selecionaPerfil)

    btn_selecionar.place(x=100, y= 70)
    global canvas_perfil
    canvas_perfil = Canvas(perfilConfig, width = 50, height = 50, bd = 4, relief = "sunken")
    canvas_perfil.place(x=270, y=70)
    global img_perfil, filename
    img_perfil = PhotoImage(file = filename)
    global image_perfil_id
    image_perfil_id = canvas_perfil.create_image(25, 25, image=img_perfil)

    #---- GUARDAR configurações
    btn_guardar = Button(perfilConfig, text = "Guardar configurações", height = 3, width=42, 
                    command = lambda: [guardarPerfil(filename),  atualizaImgPerfil()])
    btn_guardar.place(x=100, y=320)




def contarJogos(numJogos, treeCategoria):
  numJogos.set(len(treeCategoria.get_children()))

def consulta_jogo(search_by, numJogos):

    
    treeCategoria.delete(*treeCategoria.get_children())

    val = search_by.get()

    fileJogo = open(ficheiro_jogo, "r")
    linhas = fileJogo.readlines()
    fileJogo.close()
    for linha in linhas:
        filename =  linha.split(";")[0]
        jogo = linha.split(";")[1]
        categoria = linha.split(';')[2]
        if categoria == val:
            treeCategoria.insert('', 'end', values=(jogo, categoria))
        elif val == 'ALL':treeCategoria.insert('', 'end', values = (jogo, categoria))
        
    contarJogos(numJogos, treeCategoria)
        

def selecionaJogo():
  """
  selecionar imagem para o jogo, nas configurações, a partir de FileDialog
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


    panelJogos = PanedWindow(window, width = 1200, height =600, bd = "3", relief = "sunken")
    panelJogos.place(x=0, y=0)

    btn_selecionar = Button(panelJogos, text = "Selecione imagem \n do jogo", width = 20, height = 5, 
                    command = selecionaJogo)

    btn_selecionar.place(x=250, y= 210)
    global canvas_jogo
    canvas_jogo = Canvas(panelJogos, width = 180, height = 220)
    canvas_jogo.place(x=70, y=240)
    global img_jogo, filename
    img_jogo = PhotoImage(file = filename)
    global image_jogo_id
    image_jogo_id = canvas_jogo.create_image(25, 25, image=img_jogo)

    lblGame = Label(panelJogos, text = 'Name of the Game', fg = 'black', font = ('Calibri', 12), bg = 'white') 
    lblCategory = Label(panelJogos, text = 'Category', fg = 'black', font = ('Calibri', 12), bg = 'white') #añadir un combobox
    lblDescription = Label(panelJogos, text = 'Description', fg = 'black', font = ('Calibri', 12), bg = 'white')

    lblGame.place(x = 50, y = 80)
    lblCategory.place(x = 50, y = 120)
    lblDescription.place(x= 50, y = 180)



    nameGame = StringVar()
    txtGame = Entry(panelJogos, textvariable=nameGame, width=30, font = ('Calibri',10))
    nameCategory = StringVar()
    txtCategory = Entry(panelJogos, textvariable=nameCategory, width=30, font = ('Calibri', 10))
    description = StringVar()
    txtDescription = Entry(panelJogos, textvariable=description, width = 30, font = ('Helvetica', 10))
    txtGame.place(x= 180, y =80)
    txtCategory.place(x=180, y= 120)
    txtDescription.place(x=180, y = 180)

    #---- GUARDAR configurações----#
    btn_guardar = Button(panelJogos, text = "Guardar configurações", height = 3, width=24, 
                    command = lambda: [guardarJogo(nameCategory, nameGame, filename, tree, description, panelJogos)])
    btn_guardar.place(x=450, y=420)





def signUp(logInWindow):
    windowFechar.withdraw()

    signWindow = Toplevel()
    signWindow.focus_force()  # força o focus na window atual
    signWindow.grab_set()
    signWindow.resizable(0, 0)

    signWindow.title('Sign In')
    signWindow.iconbitmap('images/login.ico')

    screenWidth =signWindow.winfo_screenwidth()
    screenHeight = signWindow.winfo_screenheight()

    appWidth = 1200
    appHeight = 600
    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    signWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    signWindow.configure(bg="grey")


    #imagem
    ctnImag = Canvas(signWindow, width= 500, height=600)
    ctnImag.place(x=0, y=0)#,width=500,height=500
    global imagem
    imagem= PhotoImage(file = 'images/signIn.png')
    ctnImag.create_image(250, 300, image=imagem)
    #parte do Sign in
    #Titulo
    lblLogIn = Label(signWindow, text = 'SIGN UP', fg = 'black', font = ('Calibri', 35), bg = 'grey')
    lblLogIn.place(x=770, y=40)
    #Label e Entry

    lblMail = Label(signWindow, text = 'E-MAIL',  fg = 'black', font = ('Calibri', 20), bg = 'grey')
    lblMail.place(x = 700, y = 100)
    txtMail = Entry(signWindow, width=20, font = ('Calibri', 20))
    userMail = StringVar()
    txtMail = Entry(signWindow, width=20, font = ('Calibri', 20), textvariable=userMail)
    txtMail.place( x = 700, y = 140)

    lblUsername = Label(signWindow, text = 'USERNAME',  fg = 'black', font = ('Calibri', 20), bg = 'grey')
    lblUsername.place(x = 700, y = 200)
    userName = StringVar()
    txtUserNlblUsername = Entry(signWindow, width=20, font = ('Calibri', 20), textvariable=userName)
    txtUserNlblUsername.place( x = 700, y = 240)
    lblPw = Label(signWindow, text = 'PASSWORD',  fg = 'black', font = ('Calibri', 20), bg = 'grey')
    lblPw.place(x = 700, y = 300)
    userPass = StringVar()
    txtPw = Entry(signWindow, width=20, font = ('Calibri', 20), show = '*', textvariable=userPass)
    txtPw.place( x = 700, y = 340)
    labelPass = Label(signWindow, text ="CONFIRM PASSWORD:", fg = 'black', font = ('Calibri', 20), bg = 'grey')
    labelPass.place(x=700, y= 400)
    userPassConfirm = StringVar()
    txtPass = Entry(signWindow, width=20, font = ('Calibri', 20), textvariable = userPassConfirm, show = "*")
    txtPass.place(x=700, y= 440)

    #botao submit

    btnSubmit = Button(signWindow, text = 'CONTINUE', fg = 'black', font = ('Calibri', 15), bg = 'orange', command= lambda: criaConta(userMail.get(), userName.get(), userPass.get(), userPassConfirm.get(), signWindow, logInWindow), width = 25)

    btnSubmit.place(x = 710, y =500)

    btnNoAcc = Button(signWindow, text='Already have an account?', font = ('Calibri', 13), command= lambda: (logInInterface(windowFechar), signWindow.withdraw()), bg='grey', relief='flat')
    btnNoAcc.place(x = 700, y = 550)

def logInInterface(windowFechar):
    
    windowFechar.withdraw()


    logInWindow = Toplevel()
    logInWindow.focus_force()
    logInWindow.grab_set()
    logInWindow.title('Log In')
    logInWindow.resizable(0, 0)
    logInWindow.iconbitmap('images/login.ico')

    screenWidth =logInWindow.winfo_screenwidth()
    screenHeight =logInWindow.winfo_screenheight()

    appWidth = 1200
    appHeight = 600

    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    logInWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    logInWindow.configure(bg="grey")



    #imagem
    ctnImg = Canvas(logInWindow, width= 500, height=600)
    ctnImg.place(x=0, y=0)
    global imagemLog
    imagemLog = PhotoImage(file = 'images/Login.png') 
    ctnImg.create_image(250, 300, image=imagemLog)
    #parte do log in
    #Titulo
    lblLogIn = Label(logInWindow, text = 'LOG IN', fg = 'black', font = ('Calibri', 35), bg = 'grey')
    lblLogIn.place(x=770, y=100)
    #Label e Entry
    lblUser = Label(logInWindow, text = 'USERNAME',  fg = 'black', font = ('Calibri', 20), bg = 'grey')
    lblUser.place(x = 700, y = 200)
    userName = StringVar()
    txtUser = Entry(logInWindow, width=20, font = ('Calibri', 20), textvariable=userName)
    txtUser.place( x = 700, y = 250)
    lblPw = Label(logInWindow, text = 'PASSWORD',  fg = 'black', font = ('Calibri', 20), bg = 'grey')
    lblPw.place(x = 700, y = 300)
    userPass = StringVar()
    txtPw = Entry(logInWindow, width=20, font = ('Calibri', 20), show = '*', textvariable=userPass)
    txtPw.place( x = 700, y = 350)
    #botao submit
    btnSubmit = Button(logInWindow, text = 'CONTINUE', fg = 'black', font = ('Calibri', 15), bg = 'orange', command= lambda: validaConta(userName.get(), userPass.get(), windowFechar, logInWindow), width = 25)
    btnSubmit.place(x = 710, y = 430)
    btnNoAcc = Button(logInWindow, text='No Account yet?', font = ('Calibri', 13), command= lambda: (signUp(logInWindow), logInWindow.withdraw()), bg='grey', relief='flat')
    btnNoAcc.place(x = 700, y = 480)




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
barraMenu.add_command(label="ADD A GAME", command=PanelConfigurar)
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
frame5 = LabelFrame(window,width=280, height=50, bg='blue', borderwidth=0, highlightthickness=0)
frame5.place(x=0, y=530)
# Treeview New Games




# Add the rowheight and vertical scrollbar

s=ttk.Style()
s.configure('Treeview', rowheight=150)

global tree

tree = ttk.Treeview(frameNewGames, selectmode='browse', columns = ('Image', 'Name', 'Category'))
treeScroll = Scrollbar(tree, orient = 'vertical')
treeScroll.pack(side = 'right', fill = 'y')
tree.place(x=0, y=35)

tree = ttk.Treeview(frameNewGames, selectmode='browse', columns = ('Image', 'Name', 'Category'), yscrollcommand=treeScroll.set)
tree.place(x=0, y=35)

tree.column('Image', width =100, anchor = 'center', stretch=False)
tree.column('Name', width = 350, anchor = 'center', stretch=False)
tree.column('Category', width = 350, anchor = 'center', stretch=False)


tree.heading('Image', text = 'Image')
tree.heading('Name', text = 'Name')
tree.heading('Category', text = 'Category')




jogos = ler_jogo()
imgs=[]
for dato in jogos:
    filename =  dato[0]
    jogo = dato[1]
    categoria = dato[2]
    imgs.append(tk.PhotoImage(file=filename))
    tree.insert('', 'end', image = imgs[-1], value = ('', jogo, categoria))




#  Scrollbar Vertical
verscrlbar = ttk.Scrollbar(frameNewGames, orient ="vertical", command = tree.yview)
# CallinPlace da Scrollbar
verscrlbar.place(x=905, y=20, height=250)
# Adicionar scrollbar à  treeview
tree.configure(yscrollcommand = verscrlbar.set)
#treeview Jogos por categorias

global treeCategoria

treeCategoria = ttk.Treeview(frame1, selectmode= 'browse', columns = ('jogos', 'categoria'), show = 'headings')

treeCategoria.column('jogos', width = 120, anchor = 'center')
treeCategoria.heading('jogos', text = 'Jogos')
treeCategoria.column('categoria', width = 120, anchor = 'center')
treeCategoria.heading('categoria', text = 'Categoria')
treeCategoria.place(x = 20, y=110)

#TOTAL GAMES
lbNumJogos = Label(frame5, text = "Nº Games:", font = ("Helvetica", "15"), bg = 'blue')
lbNumJogos.place(x=40, y=10)

numJogos = StringVar()
txt_num_jogos = Entry(frame5, width=15, textvariable = numJogos)
txt_num_jogos.place(x=150, y=15)


lblWhatsNew = Label(frameNewGames, text = 'NEW GAMES', font=('Helvetica', 12, "bold"), bg="RoyalBlue4", fg="white")
lblWhatsNew.place(x=20, y=10)
lblMostViewed = Label(frame2, text = 'MOST VIEWED', font=('Helvetica', 12, "bold"), bg="gray45", fg="white")
lblMostViewed.place(x=20, y=20)
lblMostLiked = Label(frame2, text='MOST LIKED', font=('Helvetica', 12, "bold"), bg="gray45", fg="white")
lblMostLiked.place(x=20, y=150)
lblMyFavorites = Label(frame2, text = 'MY FAVORITES', font=('Helvetica', 12, "bold"), bg="gray45", fg="white")
lblMyFavorites.place(x=20, y=280)

# Search Category

column = []
fileCategoria = open('files/categorias.txt', 'r')
for line in fileCategoria:
    column.append(line.strip())
fileCategoria.close()
search_by = ttk.Combobox(frame4, values = column, width = 43, height= 100)
search_by.current(0)
search_by.place(x = 0, y = 0)
# Search Text

# Search Button
btnSearch = Button(frame4, text='Search', width=25, height=2, bg="gray13", fg="white", command= lambda: (consulta_jogo(search_by, numJogos)))
btnSearch.place(x= 50, y = 40)



# Login Button
btnLogin = Button(window, text="Login",font=('Helvetica', 10), width=6, height=1, bg="orange", fg="black", command= lambda: logInInterface(windowFechar))
btnLogin.place(x = 985, y = 1)
# Create Account Button
btnCreateAccount = Button(window, text="Create Account",font=('Helvetica', 10), width=12, height=1, bg="orange", fg="black", command=signUp)
btnCreateAccount.place(x = 1095, y = 1)

btnCreateCategory = Button(window, text="Create Category",font=('Helvetica', 10), width=12, height=1, bg="blue", fg="black", command= lambda: adicionarCategoria(newCategoria, search_by))
btnCreateCategory.place(x = 10, y = 1)

newCategoria = StringVar()
txtCategoriaAdd = Entry(window, textvariable=newCategoria, font=('Helvetica', 15), width=15)
txtCategoriaAdd.place(x=120, y = 1)

btnDeleteCategory = Button(window, text="Delete Category",font=('Helvetica', 10), width=20, height=1, bg="red", fg="black", command= lambda: removerCategoria(search_by))
btnDeleteCategory.place(x = 300, y = 1)























window.mainloop()
