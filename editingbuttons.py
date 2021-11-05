from tkinter import *
from tkinter import filedialog
from PIL import Image
from adjust import Adjust
from filters import Filters
from rotate import Rotate
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

        self.RotateButton  = Button(self , text='Rotate'  )
        self.DrawButton    = Button(self , text='Draw'    )
        self.CropButton    = Button(self , text='Crop'    )
        self.AdjustButton  = Button(self , text='Adjust'  )
        self.FiltersButton = Button(self , text='Filter'  ) 
        self.ClearButton   = Button(self , text='Clear'   )

        self.RotateButton .bind("<ButtonRelease>",self.rotate)
        self.DrawButton   .bind("<ButtonRelease>",self.startdraw)
        self.AdjustButton .bind("<ButtonRelease>",self.EditAdjust)
        self.FiltersButton.bind("<ButtonRelease>",self.ApplyFilters)
        self.ClearButton  .bind("<ButtonRelease>",self.clear)

        self.RotateButton .pack(side=LEFT)
        self.DrawButton   .pack(side=LEFT)
        self.CropButton   .pack(side=LEFT)
        self.AdjustButton .pack(side=LEFT)
        self.FiltersButton.pack(side=LEFT)
        self.ClearButton  .pack()

    def NewPictureImported(self):
        filename = filedialog.askopenfilename()
        image = Image.open(filename)

        if image is not None:
            self.master.filename = filename
            self.master.OriginalImage = image.copy()
            self.master.EditedImage = image.copy()
            self.master.viewimage.show_image()
            self.master.ImageIsSelected = True

    def SavePicture(self):
        if self.master.ImageIsSelected:
            SavedImage = self.master.EditedImage
            SavedImage.save(self.master.filename)

    def SavePictureAs(self):
        if self.master.ImageIsSelected:
            origial_width , original_height = self.master.OriginalImage.size
            original_file_type = self.master.filename.split('.')[-1]
            SavedImage = self.master.EditedImage.resize((origial_width , original_height))
            filename = filedialog.asksaveasfilename(defaultextension=original_file_type ,filetypes=[("JPG (*.jpg)","*.jpg"),("PNG (*.png)","*.png"),("JPEG (*jpeg)","*jpeg")])
            SavedImage.save(filename)
            self.master.filename = filename

    def rotate(self,event):
        if self.winfo_containing(event.x_root, event.y_root) == self.RotateButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DeactivateDraw()
                self.master.rotate_frame = Rotate(master=self.master)
    def startdraw(self,event):
        if self.winfo_containing(event.x_root, event.y_root) == self.DrawButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DeactivateDraw()
                else:
                    self.master.viewimage.StartDrawing()

    def EditAdjust(self,event):
        if self.winfo_containing(event.x_root, event.y_root) == self.AdjustButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DeactivateDraw()
                self.master.adjust_frame = Adjust(master=self.master)
                self.master.adjust_frame.grab_set() 

    def ApplyFilters(self,event):
        if self.winfo_containing(event.x_root, event.y_root) == self.FiltersButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DeactivateDraw()
                self.master.filters_frame = Filters(master=self.master)
                self.master.filters_frame.grab_set()  

    def clear(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.ClearButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DeactivateDraw()
                self.master.EditedImage = self.master.OriginalImage.copy()
                self.master.viewimage.show_image()