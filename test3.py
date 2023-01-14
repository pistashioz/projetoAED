from tkinter import ttk
import tkinter as tk
# Creating tkinter my_w
window = tk.Tk()
window.geometry("700x500") 
window.title("test")  
s=ttk.Style()

# Add the rowheight
s.configure('Treeview', rowheight=100)

tree = ttk.Treeview(window, selectmode='browse', columns = ('Image', 'Name', 'Category'))

tree.column('Image', width =50, anchor = 'center')
tree.column('Name', width = 130, anchor = 'center')
tree.column('Category', width = 130, anchor = 'center')

tree.heading('Image', text = 'Image')
tree.heading('Name', text = 'Name')
tree.heading('Category', text = 'Category')


img = tk.PhotoImage(file = 'images/stray.png')
tree.insert('', 'end', image = img, value = ('', 'Stray', 'Adveture'))
tree.place(x=5, y=5)

window.mainloop()