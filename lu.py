from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from interfaceConta import logInInterface, signUp
import tkinter as tk
import os
def on_select(event):
    root = Tk()
    def likess():
        global like
        like+=1
        numLikes.set(like) 

    def disable_button():
        btnLike['state'] = DISABLED
    
    
    
  
    nameCategory=StringVar()

    numLikes=IntVar()
    numLikes.set(like)
    
    row_id=treeCategoria.focus()
    linha=treeCategoria.item(row_id)
    
    jogo=linha["values"][0]
    print("a linha selecionada foi {}".format(jogo))
    nameTitle=StringVar()
    print()
    
    screenWidth =root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    appWidth = 1000
    appHeight = 700

    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    root.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

    frameAll=LabelFrame(root,width=1000,height=700,bg="#595959")
    frameAll.place(x=0,y=200)

    frameVideo = LabelFrame(root, width=1000, height=260, bg='#D3996E')
    frameVideo.place(x=0, y=0)

    frameJogo=LabelFrame(root, width=310,height=435,bg='#3C3D3E')
    frameJogo.place(x=30, y=100)


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
treeCategoria.bind('<<TreeviewSelect>>', on_select)

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
