from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#-----Arranque da aplicação ------#
class Application:
    def __init__(self, master=None):
        pass
window = Tk()
Application(window)
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


imagem = PhotoImage(file = 'images/Create_Account.png')
ctnImg.create_image(250, 300, image=imagem)



#parte do log in


#Titulo
lblLogIn = Label(window, text = 'LOG IN', fg = 'black', font = ('Calibri', 35), bg = 'grey')
lblLogIn.place(x=770, y=100)


#Label e Entry

lblMail = Label(window, text = 'E-MAIL',  fg = 'black', font = ('Calibri', 20), bg = 'grey')
lblMail.place(x = 700, y = 200)
txtMail = Entry(window, width=20, font = ('Calibri', 20))
txtMail.place( x = 700, y = 250)


lblPw = Label(window, text = 'PASSWORD',  fg = 'black', font = ('Calibri', 20), bg = 'grey')
lblPw.place(x = 700, y = 300)
txtPw = Entry(window, width=20, font = ('Calibri', 20), show = '*')
txtPw.place( x = 700, y = 350)


#botao submit

btnSubmit = Button(window, text = 'CONTINUE', fg = 'black', font = ('Calibri', 15), bg = 'orange', command='noaction', width = 25)
btnSubmit.place(x = 710, y = 430)

btnNoAcc = Button(window, text='No Account yet?', font = ('Calibri', 13), command='noaction', bg='grey', relief='flat')
btnNoAcc.place(x = 700, y = 480)













window.mainloop()