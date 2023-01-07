from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#-----Arranque da aplicação ------#
class Application:
    def __init__(self, master=None):
        pass
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

barraMenu = Menu(window, background='orange', fg='white')
barraMenu.add_command(label="LIBRARY", command="noaction")
barraMenu.add_command(label="COMMUNITY", command="noaction")
barraMenu.add_command(label="ADD A GAME", command="noaction")

window.configure(menu=barraMenu)

#FrameCatalogo
frame1 = LabelFrame(window, width=280, height=660, bg='green')
frame1.place(x=10, y=10)

frame2 = LabelFrame(window, width = 700, height=450, bg='black')
frame2.place(x=280, y=220)

frame3 = LabelFrame(window, width = 700, height=220, relief = "ridge", bg='red')
frame3.place(x=280, y=10)

frame4 = LabelFrame(frame1,width=280, height=150, bg='pink')
frame4.place(x=0, y=0)

#Labels

lblWhatsNew = Label(frame3, text = 'NEW GAMES', font=('Helvetica', 20))
lblWhatsNew.place(x=20, y=10)

lblMostViewed = Label(frame2, text = 'MOST VIEWED', font=('Helvetica', 15))
lblMostViewed.place(x=20, y=20)

lblMostLiked = Label(frame2, text='MOST LIKED', font=('Helvetica', 15))
lblMostLiked.place(x=20, y=160)

lblMyFavorites = Label(frame2, text = 'MY FAVORITES', font=('Helvetica', 15))
lblMyFavorites.place(x=20, y=300)

#search category

column = ['ALL', 'ACTION-ADVENTURE', 'ACTION', 'ADVENTURE', 'ARCADE', 'CASUAL', 'COZY', 'CRIME', 'CYBERPUNK', 'EXPERIMENTAL', 'FAMILY-FRIENDLY', 'FANTASY', 'FIRST-PERSON', 'HORROR', 'MINIGAMES', 'MISTERY', 'NOSTALGIA', 'RACING', 'RELAXING', 'SCI-FI']

search_by = ttk.Combobox(frame4, values = column, width = 40, height= 100)
search_by.current(0)
search_by.place(x = 0, y = 0)

#searchText

txtSearch = Entry(frame4, width=50)
txtSearch.place(x=0, y=30)
#button search

btnSearch = Button(frame4, text='Search', width=36, height=2)
btnSearch.place(x= 2, y = 60)
window.mainloop()