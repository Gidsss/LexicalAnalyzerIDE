from customtkinter import *
from constants.path import *
from PIL import Image, ImageTk

class CommandMenu(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.columns = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        self.rows = (0)

        self.grid_columnconfigure(self.columns, weight=1)
        self.grid_rowconfigure(self.rows, weight=1)

        self.uwuBgImage = CTkImage(light_image=Image.open(f"{UWU_ASSET}"), size = (99,30))
        self.uwuLabel = CTkLabel(master = self, image = self.uwuBgImage, text = '')
        self.uwuLabel.grid(row=0, column=0, sticky='', columnspan=2)

        self.runBgImage = CTkImage(light_image=Image.open(f"{RUN_ASSET}"))
        self.runButton = CTkButton(master=self, image=self.runBgImage, fg_color = '#1A1B26', text='', width = 99, height = 30)
        self.runButton.grid(row=0, column=13, sticky='', columnspan=1)

        self.saveBgImage = CTkImage(light_image=Image.open(f"{SAVE_ASSET}"))
        self.saveButton = CTkButton(master=self, image=self.saveBgImage, fg_color = '#1A1B26', text='', width = 99, height = 30)
        self.saveButton.grid(row=0, column=14, sticky='', columnspan=1)

        self.loadBgImage = CTkImage(light_image=Image.open(f"{LOAD_ASSET}"))
        self.loadButton = CTkButton(master=self, image=self.loadBgImage, fg_color = '#1A1B26', text='', width = 99, height = 30)
        self.loadButton.grid(row=0, column=15, sticky='', columnspan=1)
