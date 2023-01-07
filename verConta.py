from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from users import *

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


def atualizaImgPerfil():
  """
  atualiza canvas de imagem de perfil no PanelUser (HEADER), com imagem guardada em ficheiro
  """
  global imgPerfilHeader
  global imageHeader_id
  imgPerfilHeader = PhotoImage(file = filename)
  ctnUser.itemconfig(imageHeader_id, image=imgPerfilHeader)

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


#frame

frameConta = LabelFrame(window, width = 800, height = 500, bg = "black")
frameConta.place(x=200, y=40)


#Button Mudar pfp
buttonMudarFoto = Button(window, text = "change profile image", font=('Helvetica', 12), width = 20, bg = 'orange', command=selecionaPerfil)
buttonMudarFoto.place(x = 700, y = 100)
global canvaPerfil





window.configure(menu=barraMenu)


























window.mainloop()

