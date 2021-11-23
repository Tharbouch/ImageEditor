from tkinter import Frame, Canvas, CENTER, ROUND, messagebox
from tkinter.constants import TRUE
from PIL import Image,ImageTk , ImageGrab
import numpy as np
class ShowImage(Frame):
    def __init__(self,master=None):

        self.LinkDraw = list()
        self.CropSquer = 0
        self.CropedImage = None
        self.StartingPoint1 = 0
        self.StartingPoint2 = 0
        self.EndingPoint1   = 0
        self.EndingPoint2   = 0
        self.ratio = 0
        
        Frame.__init__(self,master=master , bg='#3d4453')
        self.shown_image = None
        self.canvas = Canvas(self,  bg='#3d4453', highlightthickness=0)
        self.canvas.place(relx = 0.5 , rely=0.45, anchor=CENTER)
  
    def ShowImage(self, img=None):

        if img is None:
            image = self.master.EditedImage.copy()
        else:
            image = img

        width , height = image.size
        
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
        self.ratio =  height / new_height
        self.shown_image = image.resize((new_width, new_height))
        self.shown_image = ImageTk.PhotoImage(self.shown_image)

        self.canvas.config(width= new_width, height= new_height)
        self.canvas.create_image(new_width/2 , new_height/2, anchor=CENTER, image=self.shown_image , bg=None)
   
    def StartDrawing(self):
        self.master.BackUpImage = self.master.EditedImage
        self.canvas.bind("<ButtonPress-1>", self.DrawCordinates)
        self.canvas.bind("<B1-Motion>", self.Draw)
        self.master.drawstatus = True

    def DesactivateDraw(self):

        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.master.drawstatus = False

        x = self.winfo_rootx()+self.canvas.winfo_x()+2
        y = self.winfo_rooty()+self.canvas.winfo_y()+2
        x1 = x + self.shown_image.width()-2
        y1 = y + self.shown_image.height()-2
        self.master.EditedImage = ImageGrab.grab((x ,y ,x1,y1))

    def DrawCordinates(self, event):
        self.x = event.x
        self.y = event.y
        
    def Draw(self, event):

        self.LinkDraw.append(self.canvas.create_line((self.x, self.y, event.x, event.y), width=4, fill="red", capstyle=ROUND, smooth=True))

        self.x = event.x
        self.y = event.y

    def StarCrop(self):
        self.master.BackUpImage = self.master.EditedImage 
        
        self.canvas.bind("<ButtonPress-1>",self.CropCordinates)
        self.canvas.bind("<B1-Motion>",self.crop)
        self.canvas.bind("<ButtonRelease>",self.EndCrop)
        self.master.cropstatus = True
    
    def DesactivateCrop(self):
        self.canvas.unbind("<ButtonPress-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")
        self.master.cropstatus = False

    def CropCordinates(self,event):
        self.StartingPoint1 = event.x
        self.StartingPoint2 = event.y
        
    def crop(self,event):
        if self.CropSquer:
            self.canvas.delete(self.CropSquer)
        self.EndingPoint1 = event.x
        self.EndingPoint2 = event.y
        self.CropSquer = self.canvas.create_rectangle(self.StartingPoint1 , self.StartingPoint2 , self.EndingPoint1 , self.EndingPoint2 , width=2)

    def EndCrop(self,event):
        self.CropedImage = np.array(self.master.EditedImage)
        if self.StartingPoint1  <= self.EndingPoint1 and self.StartingPoint2 <= self.EndingPoint2:
            StartingPoint1 = int(self.StartingPoint1  * self.ratio)
            StartingPoint2 = int(self.StartingPoint2 * self.ratio)
            EndingPoint1   = int(self.EndingPoint1 * self.ratio)
            EndingPoint2   = int(self.EndingPoint2 * self.ratio)
        elif self.StartingPoint1  > self.EndingPoint1 and self.StartingPoint2 <= self.EndingPoint2:
            StartingPoint1 = int(self.StartingPoint1  * self.ratio)
            StartingPoint2 = int(self.StartingPoint2 * self.ratio)
            EndingPoint1   = int(self.EndingPoint1 * self.ratio)
            EndingPoint2   = int(self.EndingPoint2 * self.ratio)

        elif self.StartingPoint1  <= self.EndingPoint1 and self.StartingPoint2 > self.EndingPoint2:
            StartingPoint1 = int(self.StartingPoint1  * self.ratio)
            StartingPoint2 = int(self.EndingPoint2 * self.ratio)
            EndingPoint1   = int(self.EndingPoint1 * self.ratio)
            EndingPoint2   = int(self.StartingPoint2 * self.ratio)
        else:
            StartingPoint1 = int(self.EndingPoint1 * self.ratio)
            StartingPoint2 = int(self.EndingPoint2 * self.ratio)
            EndingPoint1   = int(self.StartingPoint1  * self.ratio)
            EndingPoint2   = int(self.StartingPoint2 * self.ratio)

        x = slice(StartingPoint1, EndingPoint1, 1)
        y = slice(StartingPoint2, EndingPoint2, 1)

        self.master.EditedImage = Image.fromarray(self.CropedImage[y,x])
        self.ShowImage()
                
    def ClearCanvas(self):
        self.canvas.delete("all")
        self.ShowImage()