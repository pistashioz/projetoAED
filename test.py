from tkinter import *
from tkinter import ttk
def filterFirstName(*args):
    itemsOnTreeview = myTree.get_children()

    search = search_ent_var.get().capitalize()
    for eachItem in itemsOnTreeview:

        if search in myTree.item(eachItem)['values'][2]:
            #print(myTree.item(eachItem)['values'][2])
            search_var = myTree.item(eachItem)['values']
            myTree.delete(eachItem)

            myTree.insert("", 0, values=search_var)

column = ['id', 'passport', 'FullName', 'color']
data = [
    (1, '159', 'victoria', 'blue'),
    (2, '123', 'ana', 'blue'),
    (3, '489', 'victoria', 'yellow'),
    (4, '546', 'juan', 'red')
]

root= Tk()
root.geometry('600x500')



search_ent_var = StringVar()



search_by = ttk.Combobox(root, values = column)
search_by.current(2)
search_by.grid(row = 0, column = 0)


search_ent = Entry(root, textvariable=search_ent_var)
search_ent.grid(row=0, column=1, padx = 10)


search_ent_var.trace('w', filterFirstName)

tree_frame = Frame(root)
tree_frame.place(x=10, y=50, width = 500, height =300)
myTree = ttk.Treeview(tree_frame)
myTree['columns'] = column


for i in column:
    myTree.column(i, width=80)
    myTree.heading(i, text=i.capitalize())
myTree["show"] = "headings"
myTree.pack()

for each in data:
    myTree.insert("", END, values = each)

root.mainloop()