from tkinter import *
from PIL import Image
class Rotate(Toplevel):
    def __init__(self,master=None):
        Toplevel.__init__(self,master=master)

        self.RotateImage = None
        self.rotate90         = Button(self ,text='Rotate 90')
        self.rotate180        = Button(self ,text='Rotate 180')
        self.fliphorizontale  = Button(self ,text='Flip Horizontale')
        self.flipvirtecal     = Button(self ,text='Flip Vertical')

        self.rotate90       .bind("<ButtonPress-1>", self.Rotate90)
        self.rotate180      .bind("<ButtonPress-1>", self.Rotate180)
        self.fliphorizontale.bind("<ButtonPress-1>", self.FilpHorizontale)
        self.flipvirtecal   .bind("<ButtonPress-1>", self.FlipVertical)

        self.rotate90       .pack()
        self.rotate180      .pack()
        self.fliphorizontale.pack()
        self.flipvirtecal   .pack()   

        self.master.BackUpImage = self.master.EditedImage      

    def Rotate90(self,event):
        self.RotateImage = self.master.EditedImage.transpose(Image.ROTATE_90)
        self.master.EditedImage = self.RotateImage
        self.master.viewimage.ShowImage(img=self.RotateImage)
    def Rotate180(self,event):
        self.RotateImage = self.master.EditedImage.transpose(Image.ROTATE_180)
        self.master.viewimage.ShowImage(img=self.RotateImage)
        self.master.EditedImage = self.RotateImage
    def FilpHorizontale(self,event):
        self.RotateImage = self.master.EditedImage.transpose(Image.FLIP_LEFT_RIGHT)
        self.master.viewimage.ShowImage(img=self.RotateImage)
        self.master.EditedImage = self.RotateImage
    def FlipVertical(self,event):
        self.RotateImage = self.master.EditedImage.transpose(Image.FLIP_TOP_BOTTOM)
        self.master.viewimage.ShowImage(img=self.RotateImage)
        self.master.EditedImage = self.RotateImage