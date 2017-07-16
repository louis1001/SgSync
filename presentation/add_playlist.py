from tkinter import *
from tkinter.ttk import *

class AddPlaylist(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.initGUI()
    
    def initGUI(self):
        self.geometry('400x200+100+100')
        self.infoLbl = Label(self, text = 'Ingrese el id de la playlist')
        #self.infoLbl.grid(row=0, sticky='we')
        self.infoLbl.pack(expand = True, side= 'top', fill = 'x')
        
        self.input_field = Entry(self)
        #self.input_field.grid(row=1)
        self.input_field.pack(expand = True, side= 'top', fill = 'none', anchor='nw')
        
        self.serviceLbl = Label(self, text = 'Elija de que servicio es la playlist')
        #self.serviceLbl.grid(row=2)
        self.serviceLbl.pack(expand = True, side= 'top', fill = 'x')
        

root = AddPlaylist()
root.title('Add Playlist')
root.resizable(0,0)
root.mainloop()
