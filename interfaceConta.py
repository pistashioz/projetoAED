from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#-----Arranque da aplicação ------#
"""
class Application:
    def __init__(self, master=None):
        pass
window = Tk()
Application(window)
"""





def signUp():
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
    #parte do Sign in
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

    btnSubmit = Button(signWindow, text = 'CONTINUE', fg = 'black', font = ('Calibri', 15), bg = 'orange', command= lambda: criaConta(userMail.get(), userName.get(), userPass.get(), userPassConfirm.get()), width = 25)

    btnSubmit.place(x = 710, y =500)

    btnNoAcc = Button(signWindow, text='Already have an account?', font = ('Calibri', 13), command= logInInterface(), bg='grey', relief='flat')
    btnNoAcc.place(x = 700, y = 550)

def logInInterface(windowFechar):
    
    windowFechar.update()

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
    global imagem 
    imagem = PhotoImage(file = 'images/Login.png') 
    ctnImg.create_image(250, 300, image=imagem)
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
    #botao submit
    btnSubmit = Button(logInWindow, text = 'CONTINUE', fg = 'black', font = ('Calibri', 15), bg = 'orange', command= lambda: validaConta(userName.get(), userPass.get(), windowFechar, logInWindow), width = 25)
    btnSubmit.place(x = 710, y = 430)
    btnNoAcc = Button(logInWindow, text='No Account yet?', font = ('Calibri', 13), command= lambda: signUp(logInWindow), bg='grey', relief='flat')
    btnNoAcc.place(x = 700, y = 480)




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
 
#pasar esto para interfacve conta y hacer withdwraw y toda esa vaina para windowfechar

def validaConta(userName, userPass, windowFechar, logInWindow):
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
            logInWindow.destroy()
            windowFechar.upload()
    messagebox.showerror("Iniciar Sessão", "O UserName ou a Password estão incorretos!")
    return ""






def criaConta(userMail, userName, userPass, userPassConfirm): #signWindow, logInWindow):
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
    """
    signWindow.destroy()
    logInWindow.upload()
    """