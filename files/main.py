from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox


#todavia tengo que hacer que funcione el archivo, hacerlo mañana
class Application:
    def __init__(self, master=None):
        pass

def lerFicheiroUsers():
    ficheiro = "projetoAED/users.txt"

def lerFicheiroCategoria(): #o podria simplemente juntar esta con VerificarSenha porque literal solo las necesito para la misma vaina
    ficheiro = "projetoAED/games.txt"
    """
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
    """

def verificarSenha(txtEmail, txtPassword):

    mail = txtEmail.get()
    pw = str(txtPassword.get())

    credenciais = ['4020096@esmad.ipp.pt', '123456789']
    if mail == 'admin' and pw == 'admin':
        messagebox.showinfo('Hi Admin', 'welcome back :)')
    elif mail == credenciais[0] and pw == credenciais[1]:
        messagebox.showinfo('Hi User', 'welcome back :)' )
    else:
        messagebox.showwarning('Error', 'incorrect password or mail')
    
    """
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
    """
def criarConta(txtEmail, txtPassword, txtUserN):

    mail = txtEmail.get()
    pw = str(txtPassword.get())
    userName = txtUserN.get()

    users = []
    users.append(userName)

    """
    mail = txtEmail.get()
    pw = str(txtPassword.get())
    f = open(ficheiro, 'a', encoding='utf-8')
    newUser = mail + ';' + pw
    f.write(newUser)
    f.close()
    """

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

    btnLogIn = Button(signWindow, font=('Helvetica', 10), text="Already have an account? Log in!", fg="grey", relief="flat", command=logIn)
    btnLogIn.place(x=40, y=160)
    btnSignUp = Button(signWindow, font=('helvetica', 10), text="Sign Up", fg="blue", command=criarConta(txtEmail, txtPassword, txtUserN))
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

def dadosTreeview():
    tree.delete(*tree.get_children())
    mov = ""
    lista = lerFicheiro()
    for linha in lista: 
        campos = linha.split(";")
        if txtName.get() == "" or utilizador.get() == campos[0]:
            tree.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3]))
        elif txtCategory.get() == campos[1]:
            tree.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3]))
        elif txtRated.get() == campos[2]:
            tree.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3]))
        elif txtVisits.get() == campos[3]:
            tree.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3]))



def categoria(txtName, txtCategory, txtRated, txtVisits): #para obter dados da linha ativa/sselecionada da treeview

    row_id = tree.focus()
    linha = tree.item(row_id) #que es value_nosequecosa ? solo aqui esta definida?
    value_name.set(linha["values"][0])
    value_category.set(linha["values"][1])
    value_rate.set(linha["values"][2])
    value_rate.set(linha["values"][3])


#-----Arranque da aplicação ------#
window = Tk()
Application(window)
window.title('myGameList')
window.iconbitmap('images/video-game-play-pad-boy-gameboy-nintendo_108539.ico')

screenWidth =window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 1000
appHeight = 700

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
AccountMenu.add_command(label="Sign Up", command= signUp)
barraMenu.add_cascade(label="Account", menu= AccountMenu)

window.configure(menu=barraMenu)

#FrameCatalogo
frame1 = LabelFrame(window, text = "Featured Games", width=310, height=660, relief = "ridge", fg="blue")
frame1.place(x=680, y=10)

frame2 = LabelFrame(window, text="Categories", width = 650, height=370, relief = "ridge", fg="blue")
frame2.place(x=10, y=10)

frame3 = LabelFrame(window, text = "Game News", width=650, height=280, relief = "ridge", fg= "blue")
frame3.place(x = 10, y=390)

global tree
tree = ttk.Treeview(frame2, selectmode = "browse", columns = ("Name", "Category", "Visits", "Rated"), show = "headings")


#treeview para filtrar os jogos
tree.column("Name", width = 150, anchor = "c")
tree.column("Category", width = 150, anchor = "c")
tree.column("Visits", width = 150, anchor = "c")
tree.column("Rated", width = 150, anchor = "c")

tree.heading("Name", text="Name")
tree.heading("Category", text = "Category")
tree.heading("Visits", text="Visited")
tree.heading("Rated", text="Rated")
tree.place(x=20, y=20)


#tree.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3]))
#Label

"""
lblName = StringVar()
lblCategory = StringVar()
lblVisits = StringVar()
lblRated = StringVar()
"""
lblName = Label(frame2, text = "Name: ", font=("Helvetica", 9))
lblCategory = Label(frame2, text = "Category: ", font=("Helvetica", 9))
lblVisits = Label(frame2, text = "Visits: ", font=("Helvetica", 9))
lblRated = Label(frame2, text = "Rate: ", font=("Helvetica", 9))

#Entry

txtName = Entry(frame2, width=20)
txtCategory = Entry(frame2, width=20)
txtVisits = Entry(frame2, width=20)
txtRated = Entry(frame2, width=20)

lblName.place(x=30, y=270)
txtName.place(x=80, y = 270)


lblCategory.place(x=250, y=270)
txtCategory.place(x=320, y=270)

lblRated.place(x=30, y=310)
txtRated.place(x= 80, y=310)


#hacer las vistas como mayor a algun vaor tipo >1000 vistas
lblVisits.place(x=250, y=310)
txtVisits.place(x=320, y=310)


#buttons
btn1 = Button(frame2, text = "Add", state = "disable", fg = "green")
btn1.place(x=480, y = 270)

btn2 = Button(frame2, text = "Save", state = "disable", fg = "black")
btn2.place(x=550, y = 270)

btn3 = Button(frame2, text = "Cancel", state = "disable", fg = "red")
btn3.place(x=480, y = 310)

btn4 = Button(frame2, text = "Search", state = "active", fg = "blue", command = "lambda: categoria(txtName, txtCategory, txtRated, txtVisits)")
btn4.place(x=550, y = 310)





window.mainloop()