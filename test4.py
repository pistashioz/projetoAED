from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from users import *
from tkinter import filedialog

class Application:
    def __init__(self, master=None):
        pass
window = Tk()
Application(window)
window.title('ACCOUNT')
window.iconbitmap('images/login.ico')

screenWidth =window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 1200
appHeight = 600

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
window.configure(bg="grey")




def selecionaPerfil():
  """
  selecionar imagem para o perfil, nas configurações, a partir de FileDialog
  """
  global filename
  filename = filedialog.askopenfilename(title = "Select file", initialdir= "./imagens",
              filetypes = (("png files","*.png"),("gif files", "*.gif"), ("all files","*.*")))
  
  global img_perfil
  global image_perfil_id
  img_perfil = PhotoImage(file = filename)
  # change image on canvas
  global canvaPerfil
  canvaPerfil.itemconfig(image_perfil_id, image=img_perfil)

#opcoesBarra

barraMenu = Menu(window, background='orange', fg='white')
barraMenu.add_command(label="LIBRARY", command="noaction")
barraMenu.add_command(label="COMMUNITY", command="noaction")
barraMenu.add_command(label="ADD A GAME", command="noaction")
window.configure(menu=barraMenu)

#frame

frameConta = LabelFrame(window, width = 800, height = 500, bg = "black")
frameConta.place(x=200, y=40)


#Button Mudar pfp
buttonMudarFoto = Button(frameConta, text = "CHANGE PROFILE PHOTO", font=('Helvetica', 15), width = 25, bg = 'pink', command=selecionaPerfil)
buttonMudarFoto.place(x = 400, y = 70)

#Button Log Out

buttonLogOut = Button(frameConta, text = "LOG OUT", font=('Helvetica', 15), width = 10, bg = 'black', fg='white', command='noaction', relief = 'flat')
buttonLogOut.place(x = 150, y = 300)

#Button save changes

buttonSaveChanges = Button(frameConta, text = 'SAVE CHANGES', font = ('Helvetica', 15), width = 15, bg = 'pink', command =  lambda: guardarPerfil(filename))
buttonSaveChanges.place(x = 550, y = 400)


#Canva

canvaPerfil = Canvas(frameConta, width= 212, height=212)
canvaPerfil.place(x=100, y=70)
img_perfil = PhotoImage(file = 'images/default-user-image.png')
image_perfil_id = canvaPerfil.create_image(0,0, anchor = 'nw', image = img_perfil)


#user data

userLbl = Label(frameConta, text = 'USERNAME', bg = 'black', fg = 'white', font=('Helvetica', 15))
userLbl.place(x= 360, y = 150)

userMail = Label(frameConta, text = 'E-MAIL', bg = 'black', fg ='white', font=('Helvetica', 15))
userMail.place(x=360, y= 240)




























window.mainloop()