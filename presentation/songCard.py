import tkinter as tk
from tkinter import Frame

class SongCard(Frame):
    def __init__(self, parent, song_info):
        Frame().__init__(self, parent)
        self.initGUI()
    
    def initGUI(self):
        self.customFont = tk.font.Font(family='')
        self.geometry('400x80+0+0')
        
        