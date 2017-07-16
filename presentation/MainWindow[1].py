from tkinter import *
from tkinter.ttk import *
from dataAccess import dataAccess

playlists = dataAccess.load_songs()

class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.initGUI()
    
    def initGUI(self):
        self.title('SgSync')
        self.style = Style()
        
        self.style.theme_use('clam')        
        
        def my_function(event):
            sz = frame.winfo_width(), frame.winfo_height()
            print(sz)
            canvas.configure(scrollregion=canvas.bbox('all'), width = sz[0], height=sz[1])
        
        menubar = Menu(self)
        
        self.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label= 'Exit', command=self.quit)
        
        menubar.add_cascade(label='File', menu=fileMenu)
        
        self.minsize(600, 400)
        
        # sidebar
        self.sidebar = Frame(self, width=200, height=500, relief='sunken', borderwidth=2)
        self.sidebar.pack(expand=False, fill='both', side='left', anchor='nw')
        
        self.playlist_view = Listbox(self.sidebar, bg='white')
        self.playlist_view.pack(expand=False, fill='both', side='left', anchor='nw')
        
        for x in playlists:
            self.playlist_view.insert(END, x.name)
        
        # main content area
        self.mainarea = Frame(self, width=500, height=500, relief='sunken')
        self.mainarea.pack(expand=True, fill='both', side='right')
        
        self.song_shower = VerticalScrolledFrame(self.mainarea, relief='sunken')
        self.song_shower.pack(expand=True, fill='both', side = 'left', anchor='nw')
        
    

class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
 
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling
    """
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            
 
        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)
          # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
          # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                            anchor=NW)
 
        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)
        
        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)
        return