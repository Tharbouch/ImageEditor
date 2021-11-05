from tkinter import *
from PIL import ImageEnhance
class Adjust(Toplevel):
    def __init__(self,master=None):
        Toplevel.__init__(self,master=master)

        self.OriginalImage   = self.master.EditedImage
        self.ProcessingImage = self.master.EditedImage

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


        self.PreviewButtton = Button(self, text="Preview")
        self.PreviewButtton.bind("<ButtonRelease>", self.preview)
        self.PreviewButtton.pack(side=BOTTOM)

        self.apply_button = Button(self, text="Apply")
        self.apply_button.bind("<ButtonRelease>", self.apply)
        self.apply_button.pack(side= LEFT)

        self.apply_button = Button(self, text="Cancel")
        self.apply_button.bind("<ButtonRelease>", self.close)
        self.apply_button.pack(side= RIGHT)
    
    def apply(self,event):
        self.master.EditedImage = self.ProcessingImage
        self.close()

    def preview(self,event):
        BrightnessEnhancer   = ImageEnhance.Brightness(self.OriginalImage)
        brightness = BrightnessEnhancer.enhance(self.BrightnessScale.get())
        ContrastEnhancer     = ImageEnhance.Contrast(brightness)
        contrast = ContrastEnhancer.enhance(self.ContrastScale.get())
        SharpnessEnhancer    = ImageEnhance.Sharpness(contrast)
        sharpness = SharpnessEnhancer.enhance(self.SharpnessScale.get())
        self.ProcessingImage = sharpness
        self.master.viewimage.show_image(img=self.ProcessingImage)

    def close(self):
        self.master.viewimage.show_image()
        self.destroy()