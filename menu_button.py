import tkinter as t

root=t.Tk()
m=t.Menubutton(root,text="Menubutton",fg='green')
m.pack()
m.menu=t.Menu(m)
m['menu']=m.menu
m.menu.add_checkbutton(label='Home')
m.menu.add_checkbutton(label='Details')
m.menu.add_checkbutton(label='Info')
m.menu.add_checkbutton(label='Contact')
m.menu.add_checkbutton(label='About')

m.pack()

root.mainloop()
