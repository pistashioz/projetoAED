from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
import tkinter as tk
import os
from jogo2 import *






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

def manageCategorias():
    class Application:
        def __init__(self, master=None):
            pass
        window = Tk()
        Application(window)
        window.title('ACCOUNT')
        window.iconbitmap('images/login.ico')

        screenWidth =window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()

        appWidth = 1200
        appHeight = 600

        x = (screenWidth/2) - (appWidth/2)
        y = (screenHeight/2) - (appHeight/2)
        window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
        window.configure(bg="grey")

    btnCreateCategory = Button(window, text="Create Category",font=('Helvetica', 10), width=12, height=1, bg="blue", fg="black", command= lambda: adicionarCategoria(newCategoria, search_by))
    btnCreateCategory.place(x = 350, y = 80)

    newCategoria = StringVar()
    txtCategoriaAdd = Entry(window, textvariable=newCategoria, font=('Helvetica', 15), width=15)
    txtCategoriaAdd.place(x=350, y = 20)

    btnDeleteCategory = Button(window, text="Delete Category",font=('Helvetica', 10), width=20, height=1, bg="red", fg="black", command= lambda: removerCategoria(search_by))
    btnDeleteCategory.place(x = 350, y = 120)



    global treeCategoria

    treeCategoria = ttk.Treeview(window, selectmode= 'browse', columns = ('jogos', 'categoria'), show = 'headings')

    treeCategoria.column('jogos', width = 120, anchor = 'c')
    treeCategoria.heading('jogos', text = 'Jogos')
    treeCategoria.column('categoria', width = 120, anchor = 'c')
    treeCategoria.heading('categoria', text = 'Categoria')
    treeCategoria.place(x = 40, y=30)

    #TOTAL GAMES
    lbNumJogos = Label(window, text = "Nº Games:", font = ("Helvetica", "15"), bg = 'blue')
    lbNumJogos.place(x=40, y=400)

    numJogos = StringVar()
    txt_num_jogos = Entry(window, width=15, textvariable = numJogos)
    txt_num_jogos.place(x=150, y=400)





    # Search Category

    column = []
    fileCategoria = open('files/categorias.txt', 'r')
    for line in fileCategoria:
        column.append(line.strip())
    fileCategoria.close()
    search_by = ttk.Combobox(window, values = column, width = 43, height= 100)
    search_by.current(0)
    search_by.place(x = 40, y = 10)
    # Search Text

    # Search Button
    btnSearch = Button(window, text='Search', width=25, height=2, bg="gray13", fg="white", command= lambda: (consulta_jogo(search_by, numJogos)))
    btnSearch.place(x= 300, y = 180)





            


    frame5 = LabelFrame(window,width=280, height=50, bg='blue', borderwidth=0, highlightthickness=0)
    frame5.place(x=0, y=530)
    # Treeview New Games

    window.mainloop()

