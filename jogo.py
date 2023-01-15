# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import ttk          # treeview
from tkinter import filedialog   # filedialog boxes
#import random                    # Nº aleatórios 
import os
from tkinter import messagebox   #  messagebox

ficheiro_jogo = "files/games.txt"


def guardarJogo(nameCategory, nameGame, filename):
  """
  Guarda dados no ficheiro perfil.txt
  """
  filePerfil = open(ficheiro_jogo, "w")
  global jogo
  global categoria
  jogo = nameGame.get()
  categoria  = nameCategory.get()
  linha = filename + ';' + jogo + ';' + categoria + "\n"   # Imagem d eperfil;tema selecionado
  filePerfil.write(linha)
  filePerfil.close()
  messagebox.showinfo("Great", "Game saved succesfully")
  


def ler_jogo():
  """
  Ler ficheiro de perfil: devolve nome do ficheiro associado à imagem de perfil, assim como o tema predefinido 
  """
  if not os.path.exists(ficheiro_jogo):
      filePerfil = open(ficheiro_jogo, "w")
      filePerfil.write("imagens\avatar0.png;Europa")
      filePerfil.close
  filePerfil = open(ficheiro_jogo, "r")
  linha= filePerfil.readline()
  filePerfil.close()

  filename =  linha.split(";")[0]
  jogo = linha.split(";")[1]
  categoria = linha.split(';')[2][:-1]
  return filename, jogo, categoria