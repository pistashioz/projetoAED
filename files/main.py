from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox


#todavia tengo que hacer que funcione el archivo, hacerlo mañana
class Application:
    def __init__(self, master=None):
        pass


#funcao login
ficheiro = "projetoAED/users.txt"

def verificarSenha(txtEmail, txtPassword):

    mail = txtEmail.get()
    pw = str(txtPassword.get())

    f = open(ficheiro, 'r', encoding='utf-8')
    linhas = f.readlines()
    f.close()

    for linha in linhas:
        campos = linha.split(";")
        user = campos[0]
        password = campos[1]
    if mail == 'admin' and pw == 'admin':
        messagebox.showinfo('Hi Admin', 'welcome back:)')
    elif user == mail and pw == password:
        messagebox.showinfo('Hi User ', 'welcome back:)')
    else:
        messagebox.showwarning('Error','incorrect password or mail')

def criarConta(txtEmail, txtPassword, txtUserN):
    mail = txtEmail.get()
    pw = str(txtPassword.get())
    f = open(ficheiro, 'a', encoding='utf-8')
    newUser = mail + ';' + pw
    f.write(newUser)
    f.close()


def signUp():
    signWindow = Toplevel()
    signWindow.geometry('300x300')
    signWindow.title("Sign Up")
    signWindow.iconbitmap('images/login.ico')
    signWindow.focus_force()  # força o focus na window atual
    signWindow.grab_set()    # direciona todos os eventos para a window ativa 

    lblEmail = Label(signWindow, text="Email:", font=("Helvetica", 9))
    lblEmail.place(x=20, y=50)
    lblPassword = Label(signWindow, text="Password", font=("Helvetica", 9))
    lblPassword.place(x=20, y=85)
    lblUsername = Label(signWindow, text="Username: ", font=("Helvetica", 9))
    lblUsername.place(x=20, y=120)

    #Entry
    txtEmail = Entry(signWindow, width=20)
    txtEmail.place(x = 100, y = 50)
    txtPassword = Entry(signWindow, width=20, show='*')
    txtPassword.place(x=100, y=85)
    txtUserN = Entry(signWindow, width=20)
    txtUserN.place(x = 100, y = 120)
    #Button

    btnLogIn = Button(signWindow, font=('Helvetica', 10), text="Already have an account? Log in!", fg="grey", relief="flat", command= lambda: criarConta(txtEmail, txtPassword, txtUserN))
    btnLogIn.place(x=40, y=160)
    btnSignUp = Button(signWindow, font=('helvetica', 10), text="Sign Up", fg="blue", command="noaction")
    btnSignUp.place(x=120, y=210)

def logIn():
    logWindow = Toplevel()
    logWindow.geometry('300x300')
    logWindow.title("Log In")
    logWindow.iconbitmap('images/login.ico')
    logWindow.focus_force()  # força o focus na window atual
    logWindow.grab_set()    # direciona todos os eventos para a window ativa 


    #Label
    lblEmail = Label(logWindow, text="Email:", font=("Helvetica", 9))
    lblEmail.place(x=20, y=70)
    lblPassword = Label(logWindow, text="Password", font=("Helvetica", 9))
    lblPassword.place(x=20, y=120)

    #Entry
    txtEmail = Entry(logWindow, width=20)
    txtEmail.place(x = 100, y = 70)
    txtPassword = Entry(logWindow, width=20, show='*')
    txtPassword.place(x=100, y=120)
    
    #Button

    btnSignUp = Button(logWindow, font=('Helvetica', 10), text="Create an account!", fg="grey", relief="flat", command=signUp)
    btnSignUp.place(x=90, y=160)
    btnLogIn = Button(logWindow, font=('helvetica', 10), text="Log In", fg="blue", command= lambda: verificarSenha(txtEmail, txtPassword))
    btnLogIn.place(x=120, y=210)


#-----Arranque da aplicação --------------------------------
window = Tk()
Application(window)
window.title('myGameList')
window.iconbitmap('images/video-game-play-pad-boy-gameboy-nintendo_108539.ico')

screenWidth =window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 600
appHeight = 500

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
window.configure(bg="beige")

#opcoesBarra

barraMenu = Menu(window)

barraMenu.add_command(label="Games", command="noaction")
barraMenu.add_command(label="Servers", command="noaction")
barraMenu.add_command(label="Profiles", command="noaction")
barraMenu.add_command(label="Premium", command="noaction")
barraMenu.add_command(label="Downloads", command="noaction") #sera que hago una barra donde muestre las ultimas???
barraMenu.add_command(label="Forums", command="noaction")

#barraLogIn/SignUp 
AccountMenu = Menu(barraMenu)
AccountMenu.add_command(label="Log In", command= logIn)
#AccountMenu.add_command(label="Sign Up", command= signUp)
barraMenu.add_cascade(label="Account", menu= AccountMenu)

window.configure(menu=barraMenu)



window.mainloop()