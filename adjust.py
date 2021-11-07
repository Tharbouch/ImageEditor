from tkinter import *
from PIL import ImageEnhance
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

        self.ColorLable     = Label (self , text="Color")
        self.ColorLable     .pack()
        self.ColorScale     = Scale(self, from_=0, to_= 5, length=250, resolution=0.1,orient=HORIZONTAL)
        self.ColorScale     .set(1)
        self.ColorScale     .pack() 

        self.PreviewButtton = Button(self, text="Preview")
        self.PreviewButtton.bind("<ButtonRelease-1>", self.preview)
        self.PreviewButtton.pack(side=BOTTOM)

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

        self.ProcessingImage = colorbalance
        self.master.viewimage.ShowImage(img=self.ProcessingImage)

    def close(self,event):
        self.master.viewimage.ShowImage()
        self.destroy()