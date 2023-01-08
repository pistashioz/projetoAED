from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from users import *


#-----Arranque da aplicação ------#
class Application:
    def __init__(self, master=None):
        pass
window = Tk()
Application(window)

def signUp():


    signWindow = Toplevel()
    screenWidth =window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    signWindow.title('Sign In')
    signWindow.iconbitmap('images/login.ico')

    appWidth = 1200
    appHeight = 600

    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    signWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    signWindow.configure(bg="grey")

    signWindow.title("Sign Up")
    signWindow.iconbitmap('images/login.ico')
    signWindow.focus_force()  # força o focus na window atual
    signWindow.grab_set() 
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

    btnSubmit = Button(signWindow, text = 'CONTINUE', fg = 'black', font = ('Calibri', 15), bg = 'orange', command= lambda: criaConta(userName.get(), userPass.get(), userPassConfirm.get(), signWindow), width = 25)
    btnSubmit.place(x = 710, y =500)

    btnNoAcc = Button(signWindow, text='Already have an account?', font = ('Calibri', 13), command='noaction', bg='grey', relief='flat')
    btnNoAcc.place(x = 700, y = 550)




def logIn():
    window.title('Log In')
    window.iconbitmap('images/login.ico')

    screenWidth =window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    appWidth = 1200
    appHeight = 600

    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    window.configure(bg="grey")



    #imagem

    ctnImg = Canvas(window, width= 500, height=600)
    ctnImg.place(x=0, y=0)

    global imagem 

    imagem = PhotoImage(file = 'images/Login.png') 
    ctnImg.create_image(250, 300, image=imagem)



    #parte do log in


    #Titulo
    lblLogIn = Label(window, text = 'LOG IN', fg = 'black', font = ('Calibri', 35), bg = 'grey')
    lblLogIn.place(x=770, y=100)


    #Label e Entry

    lblUser = Label(window, text = 'USERNAME',  fg = 'black', font = ('Calibri', 20), bg = 'grey')
    lblUser.place(x = 700, y = 200)
    userName = StringVar()
    txtUser = Entry(window, width=20, font = ('Calibri', 20), textvariable=userName)
    txtUser.place( x = 700, y = 250)


    lblPw = Label(window, text = 'PASSWORD',  fg = 'black', font = ('Calibri', 20), bg = 'grey')
    lblPw.place(x = 700, y = 300)
    userPass = StringVar()
    txtPw = Entry(window, width=20, font = ('Calibri', 20), show = '*', textvariable=userPass)
    txtPw.place( x = 700, y = 350)


    #botao submit

    btnSubmit = Button(window, text = 'CONTINUE', fg = 'black', font = ('Calibri', 15), bg = 'orange', command= lambda: validaConta(userName.get(), userPass.get()), width = 25)
    btnSubmit.place(x = 710, y = 430)

    btnNoAcc = Button(window, text='No Account yet?', font = ('Calibri', 13), command=signUp, bg='grey', relief='flat')
    btnNoAcc.place(x = 700, y = 480)




logIn()


































window.mainloop()