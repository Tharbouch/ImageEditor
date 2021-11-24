from tkinter import *
from PIL import ImageEnhance,Image
import numpy as np
import cv2
class Adjust(Toplevel):
    def __init__(self,master=None):
        Toplevel.__init__(self,master=master)

        self.OriginalImage   = self.master.EditedImage
        self.ProcessingImage = None

        self.BrightnessLable = Label(self, text="Brightness")
        self.BrightnessLable.pack()
        self.BrightnessScale = Scale(self, from_=0, to_= 5, length=250, resolution=0.01,orient=HORIZONTAL)
        self.BrightnessScale.set(1)
        self.BrightnessScale.pack()

        self.ContrastLable = Label(self, text="Contrast")
        self.ContrastLable.pack()
        self.ContrastScale = Scale(self, from_=0, to_= 5, length=250, resolution=0.1,orient=HORIZONTAL)
        self.ContrastScale.set(1)
        self.ContrastScale.pack()

        self.SharpnessLable = Label(self, text="Sharpness")
        self.SharpnessLable.pack()
        self.SharpnessScale = Scale(self, from_=-10, to_= 10, length=250, resolution=0.1,orient=HORIZONTAL)
        self.SharpnessScale.set(1)
        self.SharpnessScale.pack()

        self.GammaLabel = Label(self, text="Gamma")
        self.GammaLabel.pack()
        self.GammaScale = Scale(self, from_=0 ,to_=5 , length=250 ,resolution=0.1 , orient=HORIZONTAL)
        self.GammaScale.set(1)
        self.GammaScale.pack()

        self.ColorLable = Label (self , text="Color")
        self.ColorLable .pack()
        self.ColorScale = Scale(self, from_=0, to_= 5, length=250, resolution=0.1,orient=HORIZONTAL)
        self.ColorScale .set(1)
        self.ColorScale .pack() 
        
        self.PreviewButton = Button(self, text="Preview")
        self.PreviewButton .bind("<ButtonRelease>" ,self.preview)
        self.PreviewButton .pack(side=BOTTOM)
          
        self.ApllyButton = Button(self, text="Apply")
        self.ApllyButton .bind("<ButtonRelease>", self.apply)
        self.ApllyButton .pack(side= LEFT)

        self.CloseButton = Button(self, text="Cancel")
        self.CloseButton .bind("<ButtonRelease>", self.close)
        self.CloseButton .pack(side= RIGHT)

    
    def apply(self,event):
        self.master.BackUpImage = self.master.EditedImage 
        self.master.EditedImage = self.ProcessingImage
    
    def preview(self,event):
        BrightnessEnhancer   = ImageEnhance.Brightness(self.OriginalImage)
        brightness = BrightnessEnhancer.enhance(self.BrightnessScale.get())

        ContrastEnhancer     = ImageEnhance.Contrast(brightness)
        contrast = ContrastEnhancer.enhance(self.ContrastScale.get())

        SharpnessEnhancer    = ImageEnhance.Sharpness(contrast)
        sharpness = SharpnessEnhancer.enhance(self.SharpnessScale.get())

        ColorEnhancer = ImageEnhance.Color(sharpness)
        colorbalance = ColorEnhancer.enhance(self.ColorScale.get())

        GammaCvImage = np.array(colorbalance)
        gamma = self.GammaScale.get()
        invGamma = 1 / gamma
        table = [((i / 255) ** invGamma) * 255 for i in range(256)]
        table = np.array(table, np.uint8)
        GammaCvImage = cv2.LUT(GammaCvImage, table)
        GammaPillowImage = Image.fromarray(GammaCvImage)

        self.ProcessingImage = GammaPillowImage
        self.master.viewimage.ShowImage(img=self.ProcessingImage)

    def close(self,event):
        self.master.viewimage.ShowImage()
        self.destroy()
