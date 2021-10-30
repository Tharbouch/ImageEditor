from tkinter import *
from tkinter import filedialog
import cv2

class EditingButtons(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master=master)
        
        def NewPictureImported(self):
            pass
        def SavePicture(self):
            pass
        def SavePictureAs(self):
            pass

        menu = Menu(self.master)
        self.master.config(menu=menu)
        fileMenu = Menu(menu , tearoff=0)
        fileMenu.add_command(label="Import" , command = NewPictureImported)
        fileMenu.add_command(label='Save'   , command = SavePicture)
        fileMenu.add_command(label='Save As', command = SavePictureAs)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit")
        menu.add_cascade(label="File", menu=fileMenu)

        self.Addtext_button = Button(self , text='Add Text')
        self.Draw_button    = Button(self , text='Draw'    )
        self.Crop_button    = Button(self , text='Crop'    )
        self.Adjust_button  = Button(self , text='Adjust'  )
        self.Filters_button = Button(self , text='Filter'  ) 
        self.Clear_button   = Button(self , text='Clear'   )
        self.Addtext_button.pack(side=LEFT)
        self.Draw_button   .pack(side=LEFT)
        self.Crop_button   .pack(side=LEFT)
        self.Adjust_button .pack(side=LEFT)
        self.Filters_button.pack(side=LEFT) 
        self.Clear_button  .pack()


