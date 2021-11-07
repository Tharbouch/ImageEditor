from tkinter import *
from tkinter import filedialog
from PIL import Image
from adjust import Adjust
from filters import Filters
from rotate import Rotate
class EditingButtons(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master=master , bg='#5a4040')
        
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
        self.UndoButton    = Button(self,  text='Undo'    )

        self.RotateButton .bind("<ButtonRelease-1>",self.Rotate)
        self.DrawButton   .bind("<ButtonRelease-1>",self.StartDraw)
        self.CropButton   .bind("<ButtonRelease-1>",self.StartCropingp)
        self.AdjustButton .bind("<ButtonRelease-1>",self.EditAdjust)
        self.FiltersButton.bind("<ButtonRelease-1>",self.ApplyFilters)
        self.ClearButton  .bind("<ButtonRelease-1>",self.Clear)
        self.UndoButton   .bind("<ButtonRelease-1>",self.Undo)

        self.UndoButton   .pack(side=BOTTOM)
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
            self.master.viewimage.ShowImage()
            self.master.ImageIsSelected = True

    def SavePicture(self):
        if self.master.ImageIsSelected:
            SavedImage = self.master.EditedImage
            SavedImage.save(self.master.filename)

    def SavePictureAs(self):
        if self.master.ImageIsSelected:
            OrigialWidth , OriginalHeight = self.master.OriginalImage.size
            OriginalImageTyppe = self.master.OrginalImage.format
            SavedImage = self.master.EditedImage.resize((OrigialWidth , OriginalHeight))
            filename = filedialog.asksaveasfilename(defaultextension=OriginalImageTyppe ,filetypes=[("JPG (*.jpg)","*.jpg"),("PNG (*.png)","*.png"),("JPEG (*jpeg)","*jpeg")])
            SavedImage.save(filename)
            self.master.filename = filename

    def Rotate(self,event):
        if self.winfo_containing(event.x_root, event.y_root) == self.RotateButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DeactivateDraw()
                if self.master.cropstatus:
                    self.master.viewimage.DeactivateCrop()
                self.master.rotate_frame = Rotate(master=self.master)
    def StartDraw(self,event):
        if self.winfo_containing(event.x_root, event.y_root) == self.DrawButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DeactivateDraw()
                if self.master.cropstatus:
                    self.master.viewimage.DeactivateCrop()
                else:
                    self.master.viewimage.StartDrawing()
    def StartCroping(self,event):
        if self.winfo_containing(event.x_root, event.y_root) == self.CropButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DeactivateDraw()
                if self.master.cropstatus:
                    self.master.viewimage.DeactivateCrop()
                else:
                    self.master.viewimage.StarCrop()


    def EditAdjust(self,event):
        if self.winfo_containing(event.x_root, event.y_root) == self.AdjustButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DeactivateDraw()
                if self.master.cropstatus:
                    self.master.viewimage.DeactivateCrop()
                self.master.adjust_frame = Adjust(master=self.master)
                self.master.adjust_frame.grab_set() 

    def ApplyFilters(self,event):
        if self.winfo_containing(event.x_root, event.y_root) == self.FiltersButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DeactivateDraw()
                if self.master.cropstatus:
                    self.master.viewimage.DeactivateCrop()
                self.master.filters_frame = Filters(master=self.master)
                self.master.filters_frame.grab_set()  

    def Clear(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.ClearButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DeactivateDraw()
                if self.master.cropstatus:
                    self.master.viewimage.DeactivateCrop()
                self.master.EditedImage = self.master.OriginalImage.copy()
                self.master.viewimage.ClearCanvas()
    def Undo(self,event):
        if self.winfo_containing(event.x_root , event.y_root) == self.UndoButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DeactivateDraw()
                if self.master.cropstatus:
                    self.master.viewimage.DeactivateCrop()
                self.master.EditedImage =  self.master.BackUpImage
                self.master.viewimage.ClearCanvas()