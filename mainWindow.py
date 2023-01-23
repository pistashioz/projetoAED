from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from interfaceConta import *
import tkinter as tk
import os
from jogo import *
from gameInfo import *




global userLogedIn 
userLogedIn = ''

imageLogedIn = 'images/default-user-image.png'


like=0
def on_select(event):
    '''Abre o game info'''
    
    row_id=tree.focus() #Obtem o id da linha ativa
    linha=tree.item(row_id) #Transforma em uma linha


    window.destroy()
    gameInfo(linha)


def switch():
    while login == True:
        btnCreateCategory['state'] = 'normal'
        btnDeleteCategory['state'] = 'normal'
        btnLogin['state'] = 'disabled'
        btnLogOut = Button(window, text="logOut",font=('Helvetica', 10), width=10, height=1, bg="orange", fg="black", command= lambda: logInInterface(windowFechar), state= 'normal')
        btnLogOut.place(x = 1005, y = 1)


        

def atualizaImgPerfil():

  #atualiza canvas de imagem de perfil no PanelUser (HEADER), com imagem guardada em ficheiro

  global imgPerfilHeader
  global imageHeader_id
  imgPerfilHeader = PhotoImage(file = filenamePerfil)
  ctnUser.itemconfig(imageHeader_id, image=imgPerfilHeader)




def selecionaPerfil():
  
  #selecionar imagem para o perfil, nas configurações
  
  global filenamePerfil
  filenamePerfil = filedialog.askopenfilename(title = "Select file", initialdir= "images/",
              filetypes = (("png files","*.png"),("gif files", "*.gif"), ("all files","*.*")))
  global imageLogedIn
  imageLogedIn = filenamePerfil
  global img_perfil
  global image_perfil_id
  img_perfil = PhotoImage(file = filenamePerfil)
  # change image on canvas
  global canvas_perfil
  canvas_perfil.itemconfig(image_perfil_id, image=img_perfil)

filenamePerfil = ler_perfil(imageLogedIn)




def contarJogos(numJogos, treeCategoria):
  numJogos.set(len(treeCategoria.get_children()))

def consulta_jogo(search_by, numJogos):
    global filename
    
    tree.delete(*tree.get_children())

    val = search_by.get()

    fileJogo = open(ficheiro_jogo, "r")
    linhas = fileJogo.readlines()
    fileJogo.close()
    for linha in linhas:
        filename =  linha.split(";")[0]
        jogo = linha.split(";")[1]
        categoria = linha.split(';')[2]
        descricao=linha.split(';')[3]
        if categoria == val:
        
            img_jogo = PhotoImage(file = filename)
            tree.insert('', 'end', values=(jogo, categoria,descricao))
        elif val == 'ALL':tree.insert('', 'end', values = (jogo, categoria,descricao))
 
    contarJogos(numJogos, tree)
        

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


def signUp(logInWindow):
    windowFechar.withdraw()
    logInWindow.withdraw()

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
    #interface da log in
    
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
    #funcao usada para verificar o inicio de sessao e manter o user
    def veri(userName):
        if abrirUser(userName.get()):
            global userLogedIn
            userLogedIn=userName.get()
        return 
    print(userLogedIn,'2')
    #botao submit
    btnSubmit = Button(logInWindow, text = 'CONTINUE', fg = 'black', font = ('Calibri', 15), bg = 'orange', command= lambda :  [validaConta(userName.get(), userPass.get(), windowFechar, logInWindow, login),veri(userName)],width = 25)

    btnSubmit.place(x = 710, y = 430)
    btnNoAcc = Button(logInWindow, text='No Account yet?', font = ('Calibri', 13), command= lambda: (signUp(logInWindow), logInWindow.withdraw()), bg='grey', relief='flat')
    btnNoAcc.place(x = 700, y = 480)



def PerfilConfigurar(userLogedIn, imageLogedIn):
    # -------------------Configura a imagem de perfil do utilizador
    perfilConfig = PanedWindow(window, width = 700, height = 450, bd = "3", relief = "sunken", bg = 'grey')
    perfilConfig.place(x=0, y=50)

    btn_selecionar = Button(perfilConfig, text = "Selecione imagem de perfil", width = 30, height = 3, bg = 'blue', 
                    command = selecionaPerfil)

    btn_selecionar.place(x=100, y= 70)
    global canvas_perfil
    canvas_perfil = Canvas(perfilConfig, width = 200, height = 200, bd = 4, relief = "sunken")
    canvas_perfil.place(x=350, y=80)
    global img_perfil, filenamePerfil
    img_perfil = PhotoImage(file = filenamePerfil)
    global image_perfil_id
    image_perfil_id = canvas_perfil.create_image(100, 100, image=img_perfil)

    #----R configurações
    btn_guardar = Button(perfilConfig, text = "Guardar configurações", height = 3, width=42, 
                    command = lambda: [guardarPerfil(perfilConfig, userLogedIn,filenamePerfil.split('projetoAED/')[1]),  atualizaImgPerfil()])
    btn_guardar.place(x=100, y=320)





def PanelConfigurar():
    #painel encarregado de adicionar jogos novos
    panelJogos = PanedWindow(window, width = 1200, height =600, bg= 'gray13')
    panelJogos.place(x=0, y=0)

    btn_selecionar = Button(panelJogos, text = "SELECT IMAGE \n OF THE GAME", bg = 'gray50', fg = 'white', width = 20, height = 5, 
                    command = selecionaJogo)

    btn_selecionar.place(x=880, y= 230)
    global canvas_jogo
    canvas_jogo = Canvas(panelJogos, width = 224, height = 125)
    canvas_jogo.place(x=850, y=80)
    global img_jogo, filename
    img_jogo = PhotoImage(file = filename)
    global image_jogo_id
    image_jogo_id = canvas_jogo.create_image(1, 1,anchor=NW, image=img_jogo)

    lblGame = Label(panelJogos, text = 'NAME OF THE GAME', fg = 'white', font = ('Calibri', 20), bg= 'gray13') 
    lblCategory = Label(panelJogos, text = 'CATEGORY', fg = 'white', font = ('Calibri', 20), bg= 'gray13')
    lblDescription = Label(panelJogos, text = 'DESCRIPTION', fg = 'white', font = ('Calibri', 20), bg= 'gray13')

    lblGame.place(x = 50, y = 80)
    lblCategory.place(x = 50, y = 250)
    lblDescription.place(x= 50, y = 450)



    nameGame = StringVar()
    txtGame = Entry(panelJogos, textvariable=nameGame, width=30, font = ('Calibri',20), bg = 'gray45')
    nameCategory = StringVar()
    txtCategory = Entry(panelJogos, textvariable=nameCategory, width=30, font = ('Calibri', 20), bg = 'gray45')
    description = StringVar()
    txtDescription = Entry(panelJogos, textvariable=description, width = 30, font = ('Helvetica', 20), bg = 'gray45')
    txtGame.place(x= 300, y =80)
    txtCategory.place(x=300, y= 255)
    txtDescription.place(x=300, y = 455)

    #---- GUARDAR configurações do jogo----#
    btn_guardar = Button(panelJogos, text = "SAVE", height = 5, width=24, bg = 'green',
                    command = lambda: [guardarJogo(nameCategory, nameGame, filename, tree, description, panelJogos)])
    btn_guardar.place(x=870, y=420)


#-----Arranque da aplicação ------#
class Application:
    def __init__(self, master=None):
        pass
window = Tk()
windowFechar = window
login = False
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
barraMenu.add_command(label="ADD A GAME", command=PanelConfigurar, state = 'normal')
window.configure(menu=barraMenu)
#FrameCatalogo
frame1 = LabelFrame(window, width=980, height=660, bg='gray35', borderwidth=0, highlightthickness=0)
frame1.place(x=0, y=0)
frame5 = LabelFrame(window,width=980, height=50, bg='black', borderwidth=0, highlightthickness=0)
frame5.place(x=0, y=530)
frame7 = LabelFrame(window, width=220, height=660, bg='gray35', borderwidth=0, highlightthickness=0)
frame7.place(x=980, y=0)

s=ttk.Style()
s.configure('Treeview', rowheight=150)

global tree

tree = ttk.Treeview(frame1, selectmode='browse', columns = ('Image', 'Name', 'Category','Description'))
tree.bind('<<TreeviewSelect>>', on_select)
tree.place(x=0, y=20)
style = ttk.Style(window)


style.configure("Treeview", background="gray13", 
                fieldbackground="black", foreground="white", font = ('Helvetica', 15))


tree.column('Image', width =100, anchor = 'center', stretch=False)
tree.column('Name', width = 225, anchor = 'center', stretch=False)
tree.column('Category', width = 250, anchor = 'center', stretch=False)
tree.column('Description', width = 225, anchor = 'center', stretch=False)

tree.heading('Image', text = 'IMAGE')
tree.heading('Name', text = 'NAME')
tree.heading('Category', text = 'CATEGORY')
tree.heading('Description', text = 'DESCRIPTION')






jogos = ler_jogo()
imgs=[]
for dato in jogos:
    filename =  dato[0]
    jogo = dato[1]
    categoria = dato[2]
    descricao=dato[3]
    imgs.append(tk.PhotoImage(file=filename))
    tree.insert('', 'end', image = imgs[-1], value = ('', jogo, categoria,descricao))







#TOTAL GAMES
lbNumJogos = Label(frame5, text = "Nº GAMES:", font = ("Helvetica", "15"), bg = 'black', fg = 'white')
lbNumJogos.place(x=40, y=10)

numJogos = StringVar()
txt_num_jogos = Entry(frame5, width=15, textvariable = numJogos, font= ('Helvetica', 20), bg = 'black', fg= 'white', relief = 'flat')
txt_num_jogos.place(x=190, y=5)


# Search Category

column = []
fileCategoria = open('files/categorias.txt', 'r')
for line in fileCategoria:
    column.append(line.strip())
fileCategoria.close()
search_by = ttk.Combobox(frame1, values = column, width = 160, height= 400)
search_by.current(0)
search_by.place(x = 0, y = 0)




# Search Button
btnSearch = Button(frame7, text='SEARCH', width=15, font = ('Helvetica', 15),height=2, bg="gray13", fg="white", command= lambda: (consulta_jogo(search_by, numJogos)))
btnSearch.place(x= 20, y = 10)


btnCreateCategory = Button(frame7, text="CREATE CATEGORY",state = 'normal', font=('Helvetica', 15), width=20, height=1, bg="blue", fg="black", command= lambda: adicionarCategoria(newCategoria, search_by))
btnCreateCategory.place(x = 0, y = 125)

newCategoria = StringVar()
txtCategoriaAdd = Entry(frame7, textvariable=newCategoria, font=('Helvetica', 20), width=15)
txtCategoriaAdd.place(x=0, y = 170)

btnDeleteCategory = Button(frame7, text="DELETE CATEGORY",font=('Helvetica', 15), state = 'normal',width=20, height=1, bg="red", fg="black", command= lambda: removerCategoria(search_by))
btnDeleteCategory.place(x = 0, y =80)


btnLogin = Button(frame7, text="LOGIN",font=('Helvetica', 15), width=10, height=1, bg="orange", fg="black", state = 'normal', command= lambda: logInInterface(windowFechar))
btnLogin.place(x = 55, y = 450)




#----- Button CONFIGURAÇÕES -----------------------

btnConfig = Button(frame7, text = "CHANGE PROFILE \nPICTURE", bg = 'blue', compound = LEFT, state = 'normal',
                  width = 17, height = 2, font = ("Helvetica", "15"), command = lambda: PerfilConfigurar(userLogedIn, imageLogedIn))
btnConfig.place(x=10, y=500)
# Imagem de perfil
ctnUser = Canvas(frame7, width = 200, height = 200, relief = "flat")
ctnUser.place(x=10, y=230)
imgPerfilHeader = PhotoImage(file = filenamePerfil)
imageHeader_id = ctnUser.create_image(100, 100, image=imgPerfilHeader)



















window.mainloop()
