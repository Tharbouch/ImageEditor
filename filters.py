from tkinter import *
import cv2
from PIL import Image 
import numpy as np
class Filters(Toplevel):
    def __init__(self,master=None):
        Toplevel.__init__(self,master=master)
        self.image = np.array(self.master.EditedImage)
        self.FiltredImageCV = None
        self.FiltredImagePIL = None

        self.negative_button      = Button(master=self, text="Negative")
        self.black_white_button   = Button(master=self, text="Black White")
        self.sepia_button         = Button(master=self, text="Sepia")
        self.emboss_button        = Button(master=self, text="Emboss")
        self.gaussian_blur_button = Button(master=self, text="Gaussian Blur")
        self.median_blur_button   = Button(master=self, text="Median Blur")
        self.cancel_button        = Button(master=self, text="Cancel")
        self.apply_button         = Button(master=self, text="Apply")

        self.negative_button      .bind("<ButtonRelease-1>", self.negative_button_released)
        self.black_white_button   .bind("<ButtonRelease-1>", self.black_white_released)
        self.sepia_button         .bind("<ButtonRelease-1>", self.sepia_button_released)
        self.emboss_button        .bind("<ButtonRelease-1>", self.emboss_button_released)
        self.gaussian_blur_button .bind("<ButtonRelease-1>", self.gaussian_blur_button_released)
        self.median_blur_button   .bind("<ButtonRelease-1>", self.median_blur_button_released)
        self.apply_button         .bind("<ButtonRelease-1>", self.apply_button_released)
        self.cancel_button        .bind("<ButtonRelease-1>", self.cancel_button_released)

        self.negative_button      .pack()
        self.black_white_button   .pack()
        self.sepia_button         .pack()
        self.emboss_button        .pack()
        self.gaussian_blur_button .pack()
        self.median_blur_button   .pack()
        self.cancel_button        .pack(side=RIGHT)
        self.apply_button         .pack()

    def negative_button_released(self, event):
        self.negative()
        self.ShowImage()

    def black_white_released(self, event):
        self.black_white()
        self.ShowImage()

    def sepia_button_released(self, event):
        self.sepia()
        self.ShowImage()

    def emboss_button_released(self, event):
        self.emboss()
        self.ShowImage()

    def gaussian_blur_button_released(self, event):
        self.gaussian_blur()
        self.ShowImage()

    def median_blur_button_released(self, event):
        self.gaussian_blur()
        self.ShowImage()

    def apply_button_released(self, event):
        self.master.BackUpImage = self.master.EditedImage 
        self.master.EditedImage = self.FiltredImagePIL
        self.ShowImage()
        self.close()

    def cancel_button_released(self, event):
        self.master.viewimage.ShowImage()
        self.close()

    def ShowImage(self):
        self.master.viewimage.ShowImage(img=self.FiltredImagePIL)

    def negative(self):
        self.FiltredImageCV = cv2.bitwise_not(self.image)
        self.FiltredImagePIL = Image.fromarray(self.FiltredImageCV)

    def black_white(self):
        self.FiltredImageCV = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        self.FiltredImagePIL = Image.fromarray(self.FiltredImageCV)


    def sepia(self):
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])

        self.FiltredImageCV = cv2.filter2D(self.image, -1, kernel)
        self.FiltredImagePIL = Image.fromarray(self.FiltredImageCV)

    def emboss(self):
        kernel = np.array([[0, -1, -1],
                           [1, 0, -1],
                           [1, 1, 0]])

        self.FiltredImageCV = cv2.filter2D(self.image, -1, kernel)
        self.FiltredImagePIL = Image.fromarray(self.FiltredImageCV)

    def gaussian_blur(self):
        self.FiltredImageCV = cv2.GaussianBlur(self.image, (41, 41), 0)
        self.FiltredImagePIL = Image.fromarray(self.FiltredImageCV)

    def median_blur(self):
        self.FiltredImageCV = cv2.medianBlur(self.image, 41)
        self.FiltredImagePIL = Image.fromarray(self.FiltredImageCV)


    def close(self):
        self.destroy()
