from tkinter import *
from PIL import Image
class Rotate(Toplevel):
    def __init__(self,master=None):
        Toplevel.__init__(self,master=master)

        self.RotateImage = None
        self.Rotate90         = Button(self ,text='Rotate 90')
        self.Rotate180        = Button(self ,text='Rotate 180')
        self.FlipHorizontale  = Button(self ,text='Flip Horizontale')
        self.FlipVirtecal     = Button(self ,text='Flip Vertical')

        self.Rotate90       .bind("<ButtonPress>", self.rotate90)
        self.Rotate180      .bind("<ButtonPress>", self.rotate180)
        self.FlipHorizontale.bind("<ButtonPress>", self.filphorizontale)
        self.FlipVirtecal   .bind("<ButtonPress>", self.flipvertical)

        self.Rotate90       .pack()
        self.Rotate180      .pack()
        self.FlipHorizontale.pack()
        self.FlipVirtecal   .pack()        

    def rotate90(self,event):
        self.RotateImage = self.master.EditedImage.transpose(Image.ROTATE_90)
        self.master.EditedImage = self.RotateImage
        self.master.viewimage.show_image(img=self.RotateImage)
    def rotate180(self,event):
        self.RotateImage = self.master.EditedImage.transpose(Image.ROTATE_180)
        self.master.viewimage.show_image(img=self.RotateImage)
        self.master.EditedImage = self.RotateImage
    def filphorizontale(self,event):
        self.RotateImage = self.master.EditedImage.transpose(Image.FLIP_LEFT_RIGHT)
        self.master.viewimage.show_image(img=self.RotateImage)
        self.master.EditedImage = self.RotateImage
    def flipvertical(self,event):
        self.RotateImage = self.master.EditedImage.transpose(Image.FLIP_TOP_BOTTOM)
        self.master.viewimage.show_image(img=self.RotateImage)
        self.master.EditedImage = self.RotateImage