# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import ttk          # treeview
from tkinter import filedialog   # filedialog boxes
#import random                    # Nº aleatórios 
import os
from tkinter import messagebox   #  messagebox

ficheiro_jogo = "files/games.txt"

def removerCategoria(delCategoria, search_by):
  my_new = []
  if delCategoria.get() in search_by['values']:
    my_new.append(delCategoria.get())
  search_by['values'] = my_new
  search_by.delete(0, 'end')
  messagebox.showinfo("Great", "Category saved succesfully")

def adicionarCategoria(newCategoria, search_by):
    search_by['values'] += (newCategoria.get(),)
    messagebox.showinfo("Great", "Category saved succesfully")



def guardarJogo(nameCategory, nameGame, filename, tree):
  """
  Guarda dados no ficheiro perfil.txt
  """
  fileJogo = open(ficheiro_jogo, "a") #cuando quiera editar las vainas de un juego es darle w
  global jogo
  global categoria
  jogo = nameGame.get()
  categoria  = nameCategory.get()
  linha = filename + ';' + jogo + ';' + categoria + "\n"   # Imagem de jogo;jogo;categoria
  fileJogo.write(linha)
  fileJogo.close()
  messagebox.showinfo("Great", "Game saved succesfully")
  


def ler_jogo():
  lista = []
  
  if not os.path.exists(ficheiro_jogo):
      filePerfil = open(ficheiro_jogo, "a")
      filePerfil.write("imagens/gow.png;NOGAME;NOGAME")
      filePerfil.close
  filePerfil = open(ficheiro_jogo, "r")
  linhas = filePerfil.readlines()
  filePerfil.close()
  for linha in linhas:
    filename =  linha.split(";")[0]
    jogo = linha.split(";")[1]
    categoria = linha.split(';')[2][:-1]
    dados = (filename, jogo, categoria)
    lista.append(dados)
  return lista





def adicionar_categorias():
  column.append()


