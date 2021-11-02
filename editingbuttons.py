from tkinter import *
from tkinter import filedialog
import cv2
from adjust import Adjust
from filter import Filters
class EditingButtons(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master=master)
        
        menu = Menu(self.master)
        self.master.config(menu=menu)
        fileMenu = Menu(menu , tearoff=0)
        fileMenu.add_command(label="Import" , command = self.NewPictureImported)
        fileMenu.add_command(label='Save'   , command = self.SavePicture)
        fileMenu.add_command(label='Save As', command = self.SavePictureAs)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit")
        menu.add_cascade(label="File", menu=fileMenu)

        self.Addtext_button = Button(self , text='Add Text')
        self.Draw_button    = Button(self , text='Draw'    )
        self.Crop_button    = Button(self , text='Crop'    )
        self.Adjust_button  = Button(self , text='Adjust'  )
        self.Filters_button = Button(self , text='Filter'  ) 
        self.Clear_button   = Button(self , text='Clear'   )

        self.Adjust_button.bind("<ButtonRelease>",self.EditAdjust)
        self.Filters_button.bind("<ButtonRelease>",self.ApplyFilters)

        self.Addtext_button.pack(side=LEFT)
        self.Draw_button   .pack(side=LEFT)
        self.Crop_button   .pack(side=LEFT)
        self.Adjust_button .pack(side=LEFT)
        self.Filters_button.pack(side=LEFT)
        self.Clear_button  .pack()

    def NewPictureImported(self):
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
            original_file_type = self.master.filename.split('.')[-1]
            filename = filedialog.asksaveasfilename()
            filename = filename + "." + original_file_type

            SavedImage = self.master.EditedImage
            cv2.imwrite(filename, SavedImage)
            self.master.filename = filename

    def EditAdjust(self,event):
            if self.winfo_containing(event.x_root, event.y_root) == self.Adjust_button:
                self.master.adjust_frame = Adjust(master=self.master)
                self.master.adjust_frame.grab_set()  

    def ApplyFilters(self,event):
            if self.winfo_containing(event.x_root, event.y_root) == self.Filters_button:
                self.master.filters_frame = Filters(master=self.master)
                self.master.filters_frame.grab_set()  
        
