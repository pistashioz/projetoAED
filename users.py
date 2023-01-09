from tkinter import *
from tkinter import messagebox

# Registar, Iniciar Sessão
fUsers= "files/users.txt"
ficheiro_perfil = 'files/perfil.txt'

def guardarPerfil(filename):
  """
  Guarda dados no ficheiro perfil.txt
  """
  filePerfil = open(ficheiro_perfil, "w")

  linha = filename
  filePerfil.write(linha)
  filePerfil.close()
 

def validaConta(userName, userPass):
    """
    Validar cautenticação com uma conta
    """
    fileUsers=open(fUsers, "r", encoding="utf-8")
    listaUsers = fileUsers.readlines()
    fileUsers.close()
    for linha in listaUsers:
        if linha.split(";")[1] == userName and linha.split(";")[2][:-1] == userPass:
            msg = "Bem-Vindo " + userName
            messagebox.showinfo("Iniciar Sessão", msg)
            startMain()
            return msg
    messagebox.showerror("Iniciar Sessão", "O UserName ou a Password estão incorretos!")
    return ""






def criaConta(userMail, userName, userPass, userPassConfirm, signWindow):
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
    linha = userMail + ';' + userName + ";" + userPass + "\n"
    fileUsers.write(linha)
    fileUsers.close()
    messagebox.showinfo("Criar Conta", "Conta criada com sucesso!")
    signWindow.place_forget()
    signWindow.destroy()