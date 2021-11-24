from tkinter import *
from PIL import Image
import cv2
import numpy as np
class Rotate(Toplevel):
    def __init__(self,master=None):
        Toplevel.__init__(self,master=master)

        self.RotateImage      = None
        self.rotateLEFT90     = Button(self ,text='Rotate LEFT 90°')
        self.rotateRIGHT90    = Button(self ,text='Rotate RIGHT 90°')
        self.rotate180        = Button(self ,text='Rotate 180°')
        self.fliphorizontale  = Button(self ,text='Flip Horizontale')
        self.flipvirtecal     = Button(self ,text='Flip Vertical')

        self.rotateLEFT90   .bind("<ButtonPress-1>", self.RotateLEFT90)
        self.rotateRIGHT90  .bind("<ButtonPress-1>", self.RotateRIGHT90)
        self.rotate180      .bind("<ButtonPress-1>", self.Rotate180)
        self.fliphorizontale.bind("<ButtonPress-1>", self.FilpHorizontale)
        self.flipvirtecal   .bind("<ButtonPress-1>", self.FlipVertical)

        self.rotateLEFT90   .pack()
        self.rotateRIGHT90  .pack()
        self.rotate180      .pack()
        self.fliphorizontale.pack()
        self.flipvirtecal   .pack()   

        self.master.BackUpImage = self.master.EditedImage      

    def RotateLEFT90(self,event):
        self.RotateImage = self.master.EditedImage.transpose(Image.ROTATE_90)
        self.master.EditedImage = self.RotateImage
        self.master.viewimage.ShowImage(img=self.RotateImage)
    def RotateRIGHT90(self,event):
        CvImage = np.array(self.master.EditedImage)
        self.RotateImage = cv2.rotate(CvImage, cv2.ROTATE_90_CLOCKWISE)
        self.master.EditedImage = Image.fromarray(self.RotateImage) 
        self.RotateImage = self.master.EditedImage
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