from tkinter import Frame, Canvas, CENTER, ROUND
from PIL import Image, ImageTk
import cv2

class ShowImage(Frame):
    def __init__(self,master=None):

        Frame.__init__(self,master=master, width=1280 , height= 800)
        self.shown_image = None
        self.canvas = Canvas(self, bg="white", width=1024, height=800)
        self.canvas.place(relx = 0.5 , rely=0.45, anchor=CENTER)
    
    def show_image(self, img=None):

        if img is None:
            image = self.master.EditedImage.copy()
        else:
            image = img

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width , channels = image.shape
        
        ratio = height / width

        new_width = width
        new_height = height

        if height > 1280 or width > 800:
            if ratio < 1:
                new_width = 1280
                new_height = int(new_width * ratio)
            else:
                new_height = 800
                new_width = int(new_height * (width / height))

        self.shown_image = cv2.resize(image, (new_width, new_height))
        self.shown_image = ImageTk.PhotoImage(Image.fromarray(self.shown_image))

        self.ratio = height / new_height

        self.canvas.config(width=new_width, height=new_height)
        self.canvas.create_image(new_width / 2, new_height / 2, anchor=CENTER, image=self.shown_image)