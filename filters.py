from tkinter import *
import cv2
from PIL import Image 
import numpy as np
class Filters(Toplevel):
    def __init__(self,master=None):
        Toplevel.__init__(self,master=master)
        
        self.image = np.asarray(self.master.EditedImage)
        self.FiltredImageCV = None
        self.FiltredImagePIL = None

        self.NegativeButton      = Button(master=self, text="Negative"      )
        self.BlackWhiteButton    = Button(master=self, text="Black White"   )
        self.SepiaButton         = Button(master=self, text="Sepia"         )
        self.EdgeDetectionButton = Button(master=self, text="Edge Detection")
        self.GaussianBlurButton  = Button(master=self, text="Gaussian Blur" )
        self.MedianBlurButton    = Button(master=self, text="Median Blur"   )
        self.CancelButton        = Button(master=self, text="Cancel"        )
        self.ApplyButton         = Button(master=self, text="Apply"         )

        self.NegativeButton       .bind("<ButtonRelease-1>", self.Negative     )
        self.BlackWhiteButton     .bind("<ButtonRelease-1>", self.BlackWhite   )
        self.SepiaButton          .bind("<ButtonRelease-1>", self.Sepia        )
        self.EdgeDetectionButton  .bind("<ButtonRelease-1>", self.EdgeDetection)
        self.GaussianBlurButton   .bind("<ButtonRelease-1>", self.GaussianBlur )
        self.MedianBlurButton     .bind("<ButtonRelease-1>", self.MedianBlur   )
        self.CancelButton         .bind("<ButtonRelease-1>", self.Cancel       )
        self.ApplyButton          .bind("<ButtonRelease-1>", self.Apply        )

        self.NegativeButton       .pack()
        self.BlackWhiteButton     .pack()
        self.SepiaButton          .pack()
        self.EdgeDetectionButton  .pack()
        self.GaussianBlurButton   .pack()
        self.MedianBlurButton     .pack()
        self.CancelButton         .pack(side=RIGHT)
        self.ApplyButton          .pack()

    def Apply(self, event):
        self.master.BackUpImage = self.master.EditedImage 
        self.master.EditedImage = self.FiltredImagePIL
        self.Show()
        self.Close()

    def Cancel(self, event):
        self.master.viewimage.ShowImage()
        self.Close()

    def Show(self):
        self.master.viewimage.ShowImage(Img=self.FiltredImagePIL)

    def Negative(self,event):
        self.FiltredImageCV = cv2.bitwise_not(self.image)
        self.FiltredImagePIL = Image.fromarray(self.FiltredImageCV)
        self.Show()

    def BlackWhite(self,event):
        self.FiltredImageCV  = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.FiltredImageCV  = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        self.FiltredImagePIL = Image.fromarray(self.FiltredImageCV)
        self.Show()

    def Sepia(self,event):
        kernel = np.array([[0.193, 0.369, 0.189],
                            [0.249, 0.286, 0.168],
                            [0.172, 0.334, 0.131]])

        self.FiltredImageCV = cv2.filter2D(self.image, -1, kernel)
        self.FiltredImagePIL = Image.fromarray(self.FiltredImageCV)
        self.Show()

    def EdgeDetection(self,event):
        self.FiltredImageCV  = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(self.FiltredImageCV,(3,3),0)
        self.FiltredImageCV = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
        self.FiltredImagePIL = Image.fromarray(self.FiltredImageCV)
        self.Show()

    def GaussianBlur(self,event):
        self.FiltredImageCV = cv2.GaussianBlur(self.image, (41, 41), 0)
        self.FiltredImagePIL = Image.fromarray(self.FiltredImageCV)
        self.Show()
    
    def MedianBlur(self,event):
        self.FiltredImageCV = cv2.medianBlur(self.image, 41)
        self.FiltredImagePIL = Image.fromarray(self.FiltredImageCV)
        self.Show()

    def Close(self):
        self.destroy()
