from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
import tkinter as tk
from tkinter import PhotoImage
import os
from jogo import *
ficheiro_jogo = "files/games.txt"
like=0









def gameInfo(linha):
    '''Abre o game info'''
    root = Tk()
    print(linha)
   
    title=linha['values'][1]#Seleciona o nome da linha
    category=linha['values'][2]
    description=linha['values'][3]
    

    

    #Isso sao as medidas da janela que abre quando a função é chamada 
    screenWidth =root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    appWidth = 1000
    appHeight = 700

    x = (screenWidth/2) - (appWidth/2)
    y = (screenHeight/2) - (appHeight/2)
    root.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

    #Frames que compoem a window

    frameAll=LabelFrame(root,width=1000,height=700,bg="#595959")
    frameAll.place(x=0,y=200)



    canvasjogo = Canvas(frameAll, width = 280, height = 280)
    canvasjogo.place(x=38, y=10)
    #canvasjogo.create_image(140, 140, image=)
        


    #ENTRYS

    nameTitle=StringVar()
    Title = Entry( frameAll,textvariable=nameTitle, font=('Helvetica', 30), disabledforeground="white",disabledbackground="#595959", highlightthickness=0,state= "disabled")
    Title.place(x=350, y=100)
    nameTitle.set(title)    
        
    nameCategory=StringVar()
    
    Category = Entry( frameAll,textvariable=nameCategory,font=('Helvetica', 15),disabledforeground="white",disabledbackground="#595959", highlightthickness=0,state= "disabled")
    Category.place(x=350, y=165)
    nameCategory.set(category)    

    nameDescription=StringVar()
    Description=Entry( frameAll,textvariable=nameDescription,font=('Helvetica', 12),disabledforeground="white",disabledbackground="#595959", highlightthickness=0,state= "disabled")
    Description.place(x=350, y=200)
    nameDescription.set(description)



    numLike=IntVar()
    Like = Entry(root,textvariable=numLike, font=('Helvetica', 12), bg="#595959",fg='#F89546',width=1, highlightthickness=0)
    Like.place(x=40, y=540)



    #Buttons
        

    btnLike = Button(frameAll, text='LIKE', width=10, height=2,bg="#F89546",fg='white')
    btnLike.place(x=350, y =330)


    btnAddGame = Button(frameAll, text='ADD GAME', width=15, height=2,bg="#F89546",fg='white')
    btnAddGame.place(x=480, y =330)

    btnAddFavorite = Button(frameAll, text='ADD FAVORITE', width=15, height=2,bg="#F89546", fg='white', image="")
    btnAddFavorite.place(x=600, y =330)
        
    root.mainloop()