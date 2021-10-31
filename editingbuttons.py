from tkinter import *
from tkinter import filedialog
import cv2

class EditingButtons(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master=master)
        
        def NewPictureImported():
            filename = filedialog.askopenfilename()
            image = cv2.imread(filename)

            if image is not None:
                self.master.filename = filename
                self.master.OriginalImage = image.copy()
                self.master.EditedImage = image.copy()
                self.master.viewimage.show_image()

        def SavePicture(self):
            SavedImage = self.master.EditedImage
            image_name = self.master.filename
            cv2.imwrite(image_name, SavedImage)

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

        self.Addtext_button = Button(self , text='Add Text').pack(side=LEFT)
        self.Draw_button    = Button(self , text='Draw'    ).pack(side=LEFT)
        self.Crop_button    = Button(self , text='Crop'    ).pack(side=LEFT)
        self.Adjust_button  = Button(self , text='Adjust'  ).pack(side=LEFT)
        self.Filters_button = Button(self , text='Filter'  ).pack(side=LEFT) 
        self.Clear_button   = Button(self , text='Clear'   ).pack()
        
        

