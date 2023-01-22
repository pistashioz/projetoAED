from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
import os


# Registar, Iniciar Sessão
fUsers= "files/users.txt"

def guardarPerfil(filenamePerfil): #mudarFotoPerfil
 
  #Guarda dados no ficheiro perfil.txt
  filePerfil = open(fUsers, "a")

  linha = filenamePerfil     
  filePerfil.write(linha)
  filePerfil.close()
  messagebox.showinfo("Quizz Cidades", "Configurações guardadas com sucesso")
  


def ler_perfil():
  
  #Ler ficheiro de perfil: devolve nome do ficheiro associado à imagem de perfil
  filePerfil = open(fUsers, "r")
  linha= filePerfil.readline()
  filePerfil.close()

  filenamePerfil =  linha.split(";")[3][:-1]
  return filenamePerfil
 
#pasar esto para interface conta y hacer withdwraw y toda esa vaina para windowfechar


def validaConta(userName, userPass, windowFechar, logInWindow, login):
    """
    Validar cautenticação com uma conta
    """
    fileUsers=open(fUsers, "r", encoding="utf-8")
    listaUsers = fileUsers.readlines()
    fileUsers.close()
    try:
        n = 0
        for linha in listaUsers:
            if linha.split(";")[1] == userName and linha.split(";")[2] == userPass:
                n=2
                msg = "Bem-Vindo " + userName
                messagebox.showinfo("Iniciar Sessão", msg)
                login = True
                windowFechar.deiconify()
                logInWindow.destroy()
                break
        if n == 0:
            messagebox.showerror("Iniciar Sessão", "O UserName ou a Password estão incorretos!")

    except:
        messagebox.showerror("Iniciar Sessão", "O UserName ou a Password estão incorretos!")
    return ""







def criaConta(userMail, userName, userPass, userPassConfirm, signWindow, logInWindow):
    """
    Criar uma nova conta
    """
    if userPass != userPassConfirm:
        messagebox.showerror("Criar Conta", "A password difere do inserido na sua confirmação!")
        return  
    if userName == "" or userPass == "":
        messagebox.showerror("Criar Conta", "O username e a password não podem ser vazios!")
        return         
    fileUsers=open(fUsers, "r", encoding="utf-8")
    listaUsers = fileUsers.readlines()
    fileUsers.close()
    for linha in listaUsers:
        fields = linha.split(";")
        if fields[0] == userName:
            messagebox.showerror("Criar Conta", "Já existe um utilizador com esse username!")
            return 
    fileUsers = open(fUsers, "a")
    defaultImg = 'images/default-user-image.png'
    linha = userMail + ';' + userName + ";" + userPass + ';' + defaultImg + "\n"
    fileUsers.write(linha)
    fileUsers.close()
    messagebox.showinfo("Criar Conta", "Conta criada com sucesso!")
    signWindow.destroy()
    signWindow.destroy()
    logInWindow.deiconify()
