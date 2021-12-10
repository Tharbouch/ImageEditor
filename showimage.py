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
        self.Ratio = 0
        
        Frame.__init__(self,master=master , bg='#3d4453')
        self.MainImage = None
        self.canvas = Canvas(self,  bg='#3d4453', highlightthickness=0)
        self.canvas.place(relx = 0.5 , rely=0.45, anchor=CENTER)
  
    def ShowImage(self, Img=None):

        if Img is None:
            Image = self.master.EditedImage.copy()
        else:
            Image = Img

        Width , Height = Image.size
        
        Ratio = Height / Width

        NewWidth = Width
        NewHeight = Height

        if Height > 1280 or Width > 800:
            if Ratio < 1:
                NewWidth = 1280
                NewHeight = int(NewWidth * Ratio)
            else:
                NewHeight = 800
                NewWidth = int(NewHeight * (Width / Height))
        self.Ratio =  Height / NewHeight
        self.MainImage = Image.resize((NewWidth, NewHeight))
        self.MainImage = ImageTk.PhotoImage(self.MainImage)

        self.canvas.config(width= NewWidth, height= NewHeight)
        self.canvas.create_image(NewWidth/2 , NewHeight/2, anchor=CENTER, image=self.MainImage , bg=None)
   
    def StartDrawing(self):
        self.master.BackUpImage = self.master.EditedImage
        self.canvas.bind("<ButtonPress-1>", self.DrawCordinates)
        self.canvas.bind("<B1-Motion>", self.Draw)
        self.master.DrawStatus = True

    def DeactivateDraw(self):

        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.master.DrawStatus = False

        x = self.winfo_rootx()+self.canvas.winfo_x()+2
        y = self.winfo_rooty()+self.canvas.winfo_y()+2
        x1 = x + self.MainImage.width()-2
        y1 = y + self.MainImage.height()-2
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
        self.canvas.bind("<B1-Motion>",self.CropRectangele)
        self.canvas.bind("<ButtonRelease>",self.EndCrop)
        self.master.CropStatus = True
    
    def DeactivateCrop(self):
        self.canvas.unbind("<ButtonPress-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")
        self.master.CropStatus = False

    def CropCordinates(self,event):
        self.StartingPoint1 = event.x
        self.StartingPoint2 = event.y
        
    def CropRectangele(self,event):
        if self.CropSquer:
            self.canvas.delete(self.CropSquer)
        self.EndingPoint1 = event.x
        self.EndingPoint2 = event.y
        self.CropSquer = self.canvas.create_rectangle(self.StartingPoint1 , self.StartingPoint2 , self.EndingPoint1 , self.EndingPoint2 , width=2)

    def EndCrop(self,event):
        self.CropedImage = np.array(self.master.EditedImage)
        if self.StartingPoint1  <= self.EndingPoint1 and self.StartingPoint2 <= self.EndingPoint2:
            StartingPoint1 = int(self.StartingPoint1 * self.Ratio)
            StartingPoint2 = int(self.StartingPoint2 * self.Ratio)
            EndingPoint1   = int(self.EndingPoint1   * self.Ratio)
            EndingPoint2   = int(self.EndingPoint2   * self.Ratio)
        elif self.StartingPoint1  > self.EndingPoint1 and self.StartingPoint2 <= self.EndingPoint2:
            StartingPoint1 = int(self.StartingPoint1 * self.Ratio)
            StartingPoint2 = int(self.StartingPoint2 * self.Ratio)
            EndingPoint1   = int(self.EndingPoint1   * self.Ratio)
            EndingPoint2   = int(self.EndingPoint2   * self.Ratio)

        elif self.StartingPoint1  <= self.EndingPoint1 and self.StartingPoint2 > self.EndingPoint2:
            StartingPoint1 = int(self.StartingPoint1 * self.Ratio)
            StartingPoint2 = int(self.EndingPoint2   * self.Ratio)
            EndingPoint1   = int(self.EndingPoint1   * self.Ratio)
            EndingPoint2   = int(self.StartingPoint2 * self.Ratio)
        else:
            StartingPoint1 = int(self.EndingPoint1   * self.Ratio)
            StartingPoint2 = int(self.EndingPoint2   * self.Ratio)
            EndingPoint1   = int(self.StartingPoint1 * self.Ratio)
            EndingPoint2   = int(self.StartingPoint2 * self.Ratio)

        x = slice(StartingPoint1, EndingPoint1, 1)
        y = slice(StartingPoint2, EndingPoint2, 1)

        self.master.EditedImage = Image.fromarray(self.CropedImage[y,x])
        self.ShowImage()

                
    def ClearCanvas(self):
        self.canvas.delete("all")
        self.ShowImage()