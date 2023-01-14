from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from interfaceConta import logInInterface, signUp
import tkinter as tk

#-----Arranque da aplicação ------#
class Application:
    def __init__(self, master=None):
        pass


window = Tk()
windowFechar = window
Application(window)


screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 1200
appHeight = 600

x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
window.title('myGameList')
window.resizable(0,0)
window.iconbitmap('images/video-game-play-pad-boy-gameboy-nintendo_108539.ico')
window.configure(bg="beige")

#opcoesBarra

barraMenu = Menu(window, background='orange', fg='white')
barraMenu.add_command(label="LIBRARY", command="noaction")
barraMenu.add_command(label="COMMUNITY", command="noaction")
barraMenu.add_command(label="ADD A GAME", command="noaction")

window.configure(menu=barraMenu)

#FrameCatalogo
frame1 = LabelFrame(window, width=280, height=660, bg='gray35', borderwidth=0, highlightthickness=0)
frame1.place(x=0, y=30)

frameNewGames = LabelFrame(window, width = 920, height=220, relief = "ridge", bg='RoyalBlue4', borderwidth=0, highlightthickness=0)
frameNewGames.place(x=280, y=30)

frame2 = LabelFrame(window, width = 920, height=450, bg='gray45', borderwidth=0, highlightthickness=0)
frame2.place(x=280, y=250)

frame4 = LabelFrame(window,width=280, height=100, bg='gray13', borderwidth=0, highlightthickness=0)
frame4.place(x=0, y=30)

frameLoginBackground = LabelFrame(window,width=1200,height=30, bg="thistle",borderwidth=0, highlightthickness=0)
frameLoginBackground.place(x=0, y=0)

frameLinha1 = LabelFrame(frameNewGames,width=850,height=1, bg="white",borderwidth=0, highlightthickness=0)
frameLinha1.place(x=130, y=20)

# Treeview New Games

# Add the rowheight and vertical scrollbar

s=ttk.Style()
s.configure('Treeview', rowheight=150, fieldbackground="blue", background="blue")

treeScroll = Scrollbar(frameNewGames)
treeScroll.pack(side = RIGHT, fill = Y)


tree = ttk.Treeview(frameNewGames, selectmode='browse', columns = ('Image', 'Name', 'Category'), yscrollcommand=treeScroll.set)
tree.place(x=0, y=10)


tree.column('Image', width =100, anchor = 'center', stretch=False)
tree.column('Name', width = 300, anchor = 'center', stretch=False)
tree.column('Category', width = 300, anchor = 'center', stretch=False)

tree.heading('Image', text = 'Image')
tree.heading('Name', text = 'Name')
tree.heading('Category', text = 'Category')

img = tk.PhotoImage(file = 'images/stray.png') #aqui tiene que aparecer el url para la imagen, abrir los archivos
tree.insert('', 'end', image = img, value = ('', 'Stray', 'Adventure')) #aqui las variables para titulo y el nombre
tree.place(x=0, y=35)
img2 = tk.PhotoImage(file = 'images/nightsinthewood.png') 
tree.insert('', 'end', image = img2, value = ('', 'Stray', 'Adventure')) #aqui las variables para titulo y el nombre
img3 = tk.PhotoImage(file = 'images/nightsinthewood.png') 
tree.insert('', 'end', image = img3, value = ('', 'Stray', 'Adventure')) #aqui las variables para titulo y el nombre
treeScroll.configure(command=tree.yview)
tree.pack()


#Labels

lblWhatsNew = Label(frameNewGames, text = 'NEW GAMES', font=('Helvetica', 12, "bold"), bg="RoyalBlue4", fg="white")
lblWhatsNew.place(x=20, y=0)

lblMostViewed = Label(frame2, text = 'MOST VIEWED', font=('Helvetica', 12, "bold"), bg="gray45", fg="white")
lblMostViewed.place(x=20, y=20)

lblMostLiked = Label(frame2, text='MOST LIKED', font=('Helvetica', 12, "bold"), bg="gray45", fg="white")
lblMostLiked.place(x=20, y=150)

lblMyFavorites = Label(frame2, text = 'MY FAVORITES', font=('Helvetica', 12, "bold"), bg="gray45", fg="white")
lblMyFavorites.place(x=20, y=280)

# Search Category

column = ['ALL', 'ACTION-ADVENTURE', 'ACTION', 'ADVENTURE', 'ARCADE', 'CASUAL', 'COZY', 'CRIME', 'CYBERPUNK', 'EXPERIMENTAL', 'FAMILY-FRIENDLY', 'FANTASY', 'FIRST-PERSON', 'HORROR', 'MINIGAMES', 'MISTERY', 'NOSTALGIA', 'RACING', 'RELAXING', 'SCI-FI']

search_by = ttk.Combobox(frame4, values = column, width = 43, height= 100)
search_by.current(0)
search_by.place(x = 0, y = 0)

# Search Text
txtSearch = Entry(frame4, width=46)
txtSearch.place(x=0, y=30)


# Search Button

btnSearch = Button(frame4, text='Search', width=10, height=1, bg="gray13", fg="white")
btnSearch.place(x= 100, y = 60)

# Login Button

btnLogin = Button(window, text="Login",font=('Helvetica', 10), width=6, height=1, bg="orange", fg="black", command= lambda: logInInterface(windowFechar))
btnLogin.place(x = 985, y = 1)


# Create Account Button

btnCreateAccount = Button(window, text="Create Account",font=('Helvetica', 10), width=12, height=1, bg="orange", fg="black", command=signUp)
btnCreateAccount.place(x = 1095, y = 1)



window.mainloop()






















