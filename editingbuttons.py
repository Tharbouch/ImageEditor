from tkinter import *
from tkinter import filedialog
from PIL import Image
from adjust import Adjust
from filter import Filters
class EditingButtons(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master=master)
        
        menu = Menu(self.master)
        self.master.config(menu=menu)
        fileMenu = Menu(menu , tearoff=0)
        fileMenu.add_command(label="Import" , command = self.NewPictureImported)
        fileMenu.add_command(label='Save'   , command = self.SavePicture)
        fileMenu.add_command(label='Save As', command = self.SavePictureAs)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit")
        menu.add_cascade(label="File", menu=fileMenu)

        self.Addtext_button = Button(self , text='Add Text')
        self.Draw_button    = Button(self , text='Draw'    )
        self.Crop_button    = Button(self , text='Crop'    )
        self.Adjust_button  = Button(self , text='Adjust'  )
        self.Filters_button = Button(self , text='Filter'  ) 
        self.Clear_button   = Button(self , text='Clear'   )

        self.Draw_button   .bind("<ButtonRelease>",self.startdraw)
        self.Adjust_button .bind("<ButtonRelease>",self.EditAdjust)
        self.Filters_button.bind("<ButtonRelease>",self.ApplyFilters)

        self.Addtext_button.pack(side=LEFT)
        self.Draw_button   .pack(side=LEFT)
        self.Crop_button   .pack(side=LEFT)
        self.Adjust_button .pack(side=LEFT)
        self.Filters_button.pack(side=LEFT)
        self.Clear_button  .pack()

    def NewPictureImported(self):
        filename = filedialog.askopenfilename()
        image = Image.open(filename)

        if image is not None:
            self.master.filename = filename
            self.master.OriginalImage = image.copy()
            self.master.EditedImage = image.copy()
            self.master.viewimage.show_image()
            self.master.ImageIsSelected = True

    def SavePicture(self):
        if self.master.ImageIsSelected:
            SavedImage = self.master.EditedImage
            SavedImage.save(self.master.filename)

    def SavePictureAs(self):
        if self.master.ImageIsSelected:
            origial_width , original_height = self.master.OriginalImage.size
            original_file_type = self.master.filename.split('.')[-1]
            filename = filedialog.asksaveasfilename(defaultextension=original_file_type ,filetypes=[("JPG (*.jpg)","*.jpg"),("PNG (*.png)","*.png"),("JPEG (*jpeg)","*jpeg")])
            SavedImage = self.master.EditedImage.resize((origial_width , original_height))
            SavedImage.save(filename)
            self.master.filename = filename

    def EditAdjust(self,event):
        if self.master.ImageIsSelected:
            if self.winfo_containing(event.x_root, event.y_root) == self.Adjust_button:
                self.master.adjust_frame = Adjust(master=self.master)
                self.master.adjust_frame.grab_set() 

    def ApplyFilters(self,event):
        if self.master.ImageIsSelected:
            if self.winfo_containing(event.x_root, event.y_root) == self.Filters_button:
                self.master.filters_frame = Filters(master=self.master)
                self.master.filters_frame.grab_set()  
    def startdraw(self,event):
        if self.master.ImageIsSelected:
            if self.winfo_containing(event.x_root, event.y_root) == self.Draw_button:
                self.master.viewimage.startdrawing()