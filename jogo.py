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
  filePerfil = open(ficheiro_jogo, "a") #cuando quiera editar las vainas de un juego es darle w
  global jogo
  global categoria
  jogo = nameGame.get()
  categoria  = nameCategory.get()
  linha = filename + ';' + jogo + ';' + categoria + "\n"   # Imagem de jogo;jogo;categoria
  print(linha)
  filePerfil.write(linha)
  filePerfil.close()
  messagebox.showinfo("Great", "Game saved succesfully")
  


def ler_jogo():

  if not os.path.exists(ficheiro_jogo):
      filePerfil = open(ficheiro_jogo, "a")
      filePerfil.write("imagens/gow.png;NOGAME;NOGAME")
      filePerfil.close
  filePerfil = open(ficheiro_jogo, "r")
  linhas = filePerfil.readlines()
  filePerfil.close()
  print(linhas)
  for linha in linhas:
    filename =  linha.split(";")[0]
    jogo = linha.split(";")[1]
    categoria = linha.split(';')[2][:-1]
  return filename, jogo, categoria



def adicionar_categorias():
  column.append()