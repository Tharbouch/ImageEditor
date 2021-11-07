from tkinter import Frame, Canvas, CENTER, ROUND
from tkinter.constants import TRUE
from PIL import ImageTk , ImageGrab
class ShowImage(Frame):
    def __init__(self,master=None):

        self.LinkDraw = list()
        self.CropSquer = 0
        self.CropedImage = None
        self.first_x = 0
        self.first_y = 0
        self.last_x = 0
        self.last_y = 0
        
        Frame.__init__(self,master=master, width=1280 , height= 800 ,  bg='#5a4040')
        self.shown_image = None
        self.canvas = Canvas(self, width=1024, height=800 , bg='#5a4040', highlightthickness=0)
        self.canvas.place(relx = 0.5 , rely=0.45, anchor=CENTER)

#SHOWING IMAGE   
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
        self.shown_image = image.resize((new_width, new_height))
        self.shown_image = ImageTk.PhotoImage(self.shown_image)

        self.canvas.config(width= new_width, height= new_height)
        self.canvas.create_image(new_width/2 , new_height/2, anchor=CENTER, image=self.shown_image , bg=None)

#DRAWING AREA   
    def StartDrawing(self):
        self.master.BackUpImage = self.master.EditedImage
        self.canvas.bind("<ButtonPress-1>", self.DrawCordinates)
        self.canvas.bind("<B1-Motion>", self.Draw)
        self.master.drawstatus = True

    def DeactivateDraw(self):

        self.canvas.unbind("<ButtonPress-1>")
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

        self.LinkDraw.append(self.canvas.create_line((self.x, self.y, event.x, event.y), width=2, fill="red", capstyle=ROUND, smooth=True))
    
        self.x = event.x
        self.y = event.y

    def StarCrop(self):
        self.master.BackUpImage = self.master.EditedImage  
        self.canvas.bind("<ButtonPress-1>",self.CropCordinates)
        self.canvas.bind("<B1-Motion>",self.crop)
        self.canvas.bind("<ButtonRelease-1>",self.EndCrop)
        self.cropstatus = True
    
    def DeactivateCrop(self):
        self.canvas.unbind("<ButtonPress-1>")
        self.canvas.unbind("<B1-Motion>")
        self.cropstatus = False

    def CropCordinates(self,event):
        self.first_x = event.x
        self.first_y = event.y
        
    def crop(self,event):
        if self.CropSquer:
            self.canvas.delete(self.CropSquer)
        self.last_x = event.x
        self.last_y = event.y
        self.CropSquer = self.canvas.create_rectangle(self.first_x  ,self.first_y, self.last_x , self.last_y, width=2)

    def EndCrop(self,event):
        self.CropedImage = self.master.EditedImage.crop((self.first_x  ,self.first_y, self.last_x , self.last_y))
        self.master.EditedImage = self.CropedImage
        self.ShowImage()
        
    def ClearCanvas(self):
        self.canvas.delete("all")
        self.ShowImage()
