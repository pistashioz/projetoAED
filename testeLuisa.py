from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from interfaceConta import logInInterface, signUp
import tkinter as tk
import os
from jogo2 import *
ficheiro_jogo = "files/games.txt"
like=0
def on_select(event):
    '''Abre o game info'''
    root = Tk()
    def likess():
        '''Aumenta a quantidade de likes'''
        global like
        like+=1
        numLikes.set(like) 

    def disable_button():
        '''Faz o botão ser clicável apenas uma vez'''
        btnLike['state'] = DISABLED
    
    row_id=tree.focus() #Obtem o id da linha ativa
    linha=tree.item(row_id) #Transforma em uma linha

    image=linha['values'][0]
    title=linha['values'][1]#Seleciona o nome da linha
    category=linha['values'][2]
    description=linha['values'][3]
    
    #Variavel do número de likes que é preciso guardar
    numLikes=IntVar(root) 

    #Name Title que muda de acordo com o jogo que clicamos
    nameTitle=StringVar(root)
    nameTitle.set(title)

    #Categoria q tambem muda de acordo com o jogo q clicamos
    nameCategory=StringVar(root) 
    nameCategory.set(category)
    #descrição que muda de acordo com o jogo que clicamos
    textDescription=StringVar(root)
    textDescription.set(description)
    
    

    
   

    #Isso sao as medidas da janela que abre quando a função é chamada 
    screenWidth =root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    appWidth = 1000
    appHeight = 700

    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    root.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

    #Frames que compoem a window

    frameAll=LabelFrame(root,width=1000,height=700,bg="#595959")
    frameAll.place(x=0,y=200)

    frameVideo = LabelFrame(root, width=1000, height=260, bg='#D3996E')
    frameVideo.place(x=0, y=0)

    frameJogo=LabelFrame(root, width=310,height=435,bg='#3C3D3E')
    frameJogo.place(x=30, y=100)

    #ENTRYS

    
    Title = Entry( frameAll,textvariable=nameTitle, font=('Helvetica', 30), bg="#595959",fg='white')
    Title.place(x=350, y=100)

    

    Category = Entry( frameAll,textvariable=nameCategory, font=('Helvetica', 15), bg="#595959",fg='white')
    Category.place(x=350, y=165)
    

    
    Description=Entry( frameAll,textvariable=textDescription,font=('Helvetica', 12), bg="#595959",fg='white')
    Description.place(x=350, y=200)

   
    Like = Entry(root,textvariable=numLikes, font=('Helvetica', 12), bg="#595959",fg='#F89546',width=2)
    Like.place(x=40, y=540)



    #Buttons

    btnLike = Button(frameAll, text='LIKE', width=10, height=2,bg="#F89546",fg='white', command=lambda:[likess(), disable_button()])
    btnLike.place(x=350, y =330)


    btnAddGame = Button(frameAll, text='ADD GAME', width=15, height=2,bg="#F89546",fg='white')
    btnAddGame.place(x=480, y =330)

    btnAddFavorite = Button(frameAll, text='ADD FAVORITE', width=15, height=2,bg="#F89546", fg='white', image="")
    btnAddFavorite.place(x=600, y =330)
    


def switch():
    """
    """


def contarJogos(numJogos, treeCategoria):
  numJogos.set(len(treeCategoria.get_children()))

def consulta_jogo(search_by, numJogos):

    
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
window.configure(bg="black")
#opcoesBarra
barraMenu = Menu(window, background='orange', fg='white')
barraMenu.add_command(label="LIBRARY", command="noaction")
barraMenu.add_command(label="COMMUNITY", command="noaction")
barraMenu.add_command(label="ADD A GAME", command=PanelConfigurar)
window.configure(menu=barraMenu)
#FrameCatalogo
frame1 = LabelFrame(window, width=1500, height=660, bg='gray35', borderwidth=0, highlightthickness=0)
frame1.place(x=0, y=30)



frame5 = LabelFrame(window,width=165, height=50, bg='orange1', borderwidth=0, highlightthickness=0)
frame5.place(x=0, y=530)

s=ttk.Style()
s.configure('Treeview', rowheight=150)

global tree

tree = ttk.Treeview(frame1, selectmode='browse', columns = ('Image', 'Name', 'Category','Description'))
tree.bind('<<TreeviewSelect>>', on_select)
tree.place(x=165, y=40)
style = ttk.Style(window)


style.configure("Treeview", background="gray13", 
                fieldbackground="black", foreground="white")


tree.column('Image', width =200, anchor = 'center', stretch=False)
tree.column('Name', width = 200, anchor = 'center', stretch=False)
tree.column('Category', width = 200, anchor = 'center', stretch=False)
tree.column('Description', width = 200, anchor = 'center', stretch=False)

tree.heading('Image', text = 'Image')
tree.heading('Name', text = 'Name')
tree.heading('Category', text = 'Category')
tree.heading('Description', text = 'Description')





#TOTAL GAMES
lbNumJogos = Label(frame5, text = "Nº Games:", font = ("Helvetica", "12"), bg = 'orange1')
lbNumJogos.place(x=0, y=10)

numJogos = StringVar()
txt_num_jogos = Entry(frame5, width=10, textvariable = numJogos)
txt_num_jogos.place(x=80, y=15)



# Search Category

column = []
fileCategoria = open('files/categorias.txt', 'r')
for line in fileCategoria:
    column.append(line.strip())
fileCategoria.close()
search_by = ttk.Combobox(frame1, values = column, width = 164, height= 400)
search_by.current(0)
search_by.place(x = 160, y = 0)
# Search Text

# Search Button
btnSearch = Button(frame1, text='Search', width=21, height=2, bg="gray13", fg="white", command= lambda: (consulta_jogo(search_by, numJogos)))
btnSearch.place(x=0, y = 0)

#  Scrollbar Vertical
verscrlbar = ttk.Scrollbar(window, orient ="vertical", command = tree.yview)
# CallinPlace da Scrollbar
verscrlbar.place(x=1155, y=60, height=300)
# Adicionar scrollbar à  treeview
tree.configure(yscrollcommand = verscrlbar.set)
#treeview Jogos por categorias

jogos = ler_jogo()

imgs=[]
for dato in jogos:
    filename =  dato[0]
    jogo = dato[1]
    categoria = dato[2]
    descricao=dato[3]
    imgs.append(tk.PhotoImage(file=filename))
    tree.insert('', 'end', image = imgs[-1], value = ('', jogo, categoria, descricao))


# Login Button
btnLogin = Button(window, text="Login",font=('Helvetica', 10), width=6, height=1, bg="orange", fg="black", command= lambda: logInInterface(windowFechar))
btnLogin.place(x = 1000, y = 1)
# Create Account Button
btnCreateAccount = Button(window, text="Create Account",font=('Helvetica', 10), width=12, height=1, bg="orange", fg="black", command=signUp)
btnCreateAccount.place(x = 1065, y = 1)

btnCreateCategory = Button(frame1, text="Create Category",font=('Helvetica', 10), width=12, height=1, bg="orange1", fg="black", command= lambda: adicionarCategoria(newCategoria, search_by))
btnCreateCategory.place(x =24, y =170)

newCategoria = StringVar()
txtCategoriaAdd = Entry(frame1, textvariable=newCategoria, font=('Helvetica', 15), width=10)
txtCategoriaAdd.place(x=20, y =100)

btnDeleteCategory = Button(frame1, text="Delete Category",font=('Helvetica', 10), width=12, height=1, bg="orange3", fg="black", command= lambda: removerCategoria(search_by))
btnDeleteCategory.place(x =24, y =210)




























window.mainloop()
