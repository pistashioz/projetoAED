# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import ttk          # treeview
from tkinter import filedialog   # filedialog boxes
import os
from jogo import *

ficheiro_jogo = "files/games.txt"


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
  canvas_jogo.itemconfig(image_perfil_id, image=img_perfil)



def PanelConfigurar():
    # ------------------------------------------------------------


    panelJogos = PanedWindow(window, width = 1200, height =600, bd = "3", relief = "sunken")
    panelJogos.place(x=0, y=50)

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



def panelJogar():
    # Panel Jogar  -------------------------------------
  panelJogar = PanedWindow(window, width = 700, height = 450, relief = "flat" )
  panelJogar.place(x=0, y=50)


  lb1 = Label(panelJogar, text = "Cidade", font = ("Helvetica", "15"))
  lb1.place(x=290, y=30)

  cidade = StringVar()
  cidade.set("")
  lblCidade = Label(panelJogar, textvariable =cidade, width = 25,  fg = "blue", font = ("Helvetica", "12"))
  lblCidade.place(x=210, y=60)

  frame2 = LabelFrame(panelJogar, text = "É a Capital do país: ", width = 450, height = 150, bd = 3, relief = "sunken")
  frame2.place(x=120, y=100)
  resposta = StringVar(frame2, "A")   # variavel que contém o conteudo / valor do radiobutton selecionado
  resp1 = Radiobutton(frame2, text = "Opção A", variable = resposta, value = "A", font = ("Helvetica", "10"), fg = "blue")
  resp2 = Radiobutton(frame2, text = "Opção B", variable = resposta, value = "B", font = ("Helvetica", "10"), fg = "blue")
  resp3 = Radiobutton(frame2, text = "Opção C", variable = resposta, value = "C", font = ("Helvetica", "10"), fg = "blue")
  resp4 = Radiobutton(frame2, text = "Opção D", variable = resposta, value = "D", font = ("Helvetica", "10"), fg = "blue")

  resp1.place(x=20, y= 20)
  resp2.place(x=250, y= 20)
  resp3.place(x=20, y= 100)
  resp4.place(x=250, y= 100)

  global btnImage1, btnImage2
  btnImage1 = PhotoImage(file = "images/stray.png")
  btnNovaPergunta = Button(panelJogar, text = "Nova Pergunta", image = btnImage1, compound = LEFT, fg = "red",
                        width = 220, height = 48, font = ("Helvetica", "10"),
                        command =lambda: obter_questao (tema, resp1, resp2, resp3, resp4, cidade))
  btnNovaPergunta.place(x=120, y=280)
  

  btnImage2 = PhotoImage(file = "images/stray.png")
  btnResponder = Button(panelJogar, text = "Validar Resposta", image = btnImage2,compound = LEFT,  fg = "red",
                      width = 220, height = 48, font = ("Helvetica", "10"),  command = lambda: validar_resposta(resposta, respCertas, respErradas))
  btnResponder.place(x=345, y=280)


  panelRespostas = PanedWindow(panelJogar, width = 700, height=50, relief="sunken")
  panelRespostas.place(x=0, y= 400)
  lblCertas = Label(panelJogar, text = "Acertou:")
  lblCertas.place(x=100, y=410)
  respCertas = StringVar()
  respCertas.set("0")
  lblrespCertas = Label(panelJogar, textvariable= respCertas, state="disabled", width=3)
  lblrespCertas.place(x=180, y=410)

  lblErradas = Label(panelJogar, text = "Errou:")
  lblErradas.place(x=500, y=410)
  respErradas = StringVar()
  respErradas.set("0")
  lblRespErradas = Label(panelJogar, textvariable= respErradas, state="disabled", width=3)
  lblRespErradas.place(x=580, y=410)



# ---------------Main---------------------
#-----------------------------------------
window = Tk()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 700                             # tamanho (pixeis) da window a criar 900 / 500
appHeight = 500 
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title('Quizz - Capitais')

#window.overrideredirect(True)         # remove os atributos da window de maximizar, minimizar e fecho
#window.attributes('-disabled', True)   # desativa os atrubutos da window de maximizar, minimizar e fecho

filename, jogo, categoria = ler_jogo()


PanelStatus = PanedWindow(window, width=700, height=50, relief = "flat")
PanelStatus.place(x=0, y=0)

#----- Button JOGAR ------------------------------
imageNovo = PhotoImage(file = "images/stray.png" )
btnJogar = Button(PanelStatus, text = "Novo Jogo", width = 100, height = 48, image = imageNovo, compound = LEFT,
                   font = ("Helvetica", "10"),  command = panelJogar)
btnJogar.place(x=100, y=0)
#----- Button SAIR ------------------------------
imageSair = PhotoImage(file = "images/signIn.png" )
btnSair = Button(PanelStatus, text = "Fechar", width = 100, height = 48,   image = imageSair, compound = LEFT,
                  font = ("Helvetica", "10"),  command = window.destroy)
btnSair.place(x=250, y=0)
#----- Button CONFIGURAÇÕES -----------------------
imageConfig = PhotoImage(file = "images/signIn.png" )
btnConfig = Button(PanelStatus, text = "Configurar \nopções", image = imageConfig, compound = LEFT, 
                  width = 100, height = 48, font = ("Helvetica", "10"), command = PanelConfigurar)
btnConfig.place(x=400, y=0)
# Imagem de jogo
ctnUser = Canvas(PanelStatus, width = 50, height = 50, relief = "flat")
ctnUser.place(x=600, y=0)
imgJogo = PhotoImage(file = filename)
imageHeader_id = ctnUser.create_image(25, 25, image=imgJogo)


# ------------ Imagem do Quizz ------------------
ctnLogo = Canvas(window, width = 700, height = 450, relief = "flat")
ctnLogo.place(x=0, y=70)
img_logo = PhotoImage(file = "images/signIn.png")
ctnLogo.create_image(350, 225, image=img_logo)

window.mainloop()   # event listening loop by calling the mainloop()