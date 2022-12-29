from tkinter import *
from tkinter import ttk

window = Tk()
window.title('treeview test')
window.geometry('500x500')

myTree = ttk.Treeview(window)

myTree = ttk.Treeview(window, selectmode= 'browse', columns= ('name', 'category', 'rated', 'views'), show = 'headings')

#Formate our columns

myTree.column('name', anchor='c', width = 120)
myTree.column('category', anchor='c', width=120)
myTree.column('rated', anchor ='c', width=80)
myTree.column('views', anchor ='c', width=80)
myTree.heading('name', text = 'name')
myTree.heading('category', text = 'category')
myTree.heading('rated', text = 'rated')
myTree.heading('views', text = 'views')
myTree.place(x=5, y=5)


