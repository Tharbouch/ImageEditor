from tkinter import Frame, Canvas, CENTER, ROUND
from PIL import Image, ImageTk
import cv2

class ShowImage(Frame):
    def __init__(self,master):
        Frame.__init__(self,master=master, width=1280 , height= 768)

        self.canvas = Canvas(self, bg="white", width=1024, height=768)
        self.canvas.place(relx = 0.5 , rely=0.45, anchor=CENTER)
    