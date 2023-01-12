from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from interfaceConta import logInInterface, signUp

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

# Canvas
canvasWhatsNew1 = Canvas(frameNewGames, width=150, height=125)
canvasWhatsNew1.place(x=30, y=35)

whatsNew1Img = PhotoImage(file="images/gow.png")
canvasWhatsNew1.create_image(60,65, image= whatsNew1Img)

canvasWhatsNew2 = Canvas(frameNewGames, width=150, height=125)
canvasWhatsNew2.place(x=260, y=35)

whatsNew2Img = PhotoImage(file="images/eldenring.png")
canvasWhatsNew2.create_image(60,65, image= whatsNew2Img)

canvasWhatsNew3 = Canvas(frameNewGames, width=150, height=125)
canvasWhatsNew3.place(x=510, y=35)

whatsNew3Img = PhotoImage(file="images/stray.png")
canvasWhatsNew3.create_image(30,60, image= whatsNew3Img)

canvasWhatsNew4 = Canvas(frameNewGames, width=150, height=125)
canvasWhatsNew4.place(x=740, y=35)

whatsNew4Img = PhotoImage(file="images/nightsinthewood.PNG")
canvasWhatsNew4.create_image(70,60, image= whatsNew4Img)


canvasLoginImage = Canvas(window, width=27, height=28, bg="orange", highlightthickness=0)
canvasLoginImage.place(x=955, y=1)

loginImg = PhotoImage(file="images/4115235-exit-logout-sign-out_114030.png")
canvasLoginImage.create_image(15,15, image= loginImg)

canvasCreateImage = Canvas(window, width=27, height=28, bg="orange", highlightthickness=0)
canvasCreateImage.place(x=1065, y=1)

createImg = PhotoImage(file="images/-create_90479.png")
canvasCreateImage.create_image(15,15, image= createImg)

# Label What's New -> Game's Name
labelWhatsNew1 = Label(frameNewGames, text = 'God of War', font=('Helvetica', 11), bg="RoyalBlue4", fg="orange")
labelWhatsNew1.place(x=30, y=165)

labelWhatsNew2 = Label(frameNewGames, text = 'Elden Ring', font=('Helvetica', 11), bg="RoyalBlue4", fg="orange")
labelWhatsNew2.place(x=260, y=165)

labelWhatsNew3 = Label(frameNewGames, text = 'Stray', font=('Helvetica', 11), bg="RoyalBlue4", fg="orange")
labelWhatsNew3.place(x=510, y=165)

labelWhatsNew4 = Label(frameNewGames, text = 'Night in the Woods', font=('Helvetica', 11), bg="RoyalBlue4", fg="orange")
labelWhatsNew4.place(x=740, y=165)

# Label What's New -> Category
labelWhatsNew5 = Label(frameNewGames, text = 'Action', font=('Helvetica', 10), bg="RoyalBlue4", fg="red")
labelWhatsNew5.place(x=30, y=185)

labelWhatsNew6 = Label(frameNewGames, text = 'Souls-like', font=('Helvetica', 10), bg="RoyalBlue4", fg="red")
labelWhatsNew6.place(x=260, y=185)

labelWhatsNew7 = Label(frameNewGames, text = 'Adventure', font=('Helvetica', 10), bg="RoyalBlue4", fg="red")
labelWhatsNew7.place(x=510, y=185)

labelWhatsNew8 = Label(frameNewGames, text = 'Adventure', font=('Helvetica', 10), bg="RoyalBlue4", fg="red")
labelWhatsNew8.place(x=740, y=185)


#Labels

lblWhatsNew = Label(frameNewGames, text = 'NEW GAMES', font=('Helvetica', 12, "bold"), bg="RoyalBlue4", fg="white")
lblWhatsNew.place(x=20, y=10)

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
































