from tkinter import *
from tkinter import filedialog,messagebox
from os import getlogin,path
import piexif
from PIL import Image
from adjust import Adjust
from filters import Filters
from rotate import Rotate
class EditingButtons(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master=master , bg='#3d4453')
        
        menu = Menu(self.master)
        self.master.config(menu=menu)
        fileMenu = Menu(menu , tearoff=0)
        fileMenu.add_command(label="Import" , command = self.NewPictureImported)
        fileMenu.add_command(label='Save'   , command = self.SavePicture)
        fileMenu.add_command(label='Save As', command = self.SavePictureAs)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit"   , command = self.Exit)
        menu.add_cascade(label="File", menu=fileMenu)

        self.RotateButton      = Button(self , text='Rotate'          )
        self.DrawButton        = Button(self , text='Draw'            )
        self.CropButton        = Button(self , text='Crop'            )
        self.AdjustButton      = Button(self , text='Adjust'          )
        self.FiltersButton     = Button(self , text='Filter'          ) 
        self.ClearButton       = Button(self , text='Clear'           )
        self.UndoButton        = Button(self,  text='Undo'            )
        self.ExtractExifButton = Button(self,  text='Extract Exif'    )

        self.RotateButton     .bind("<ButtonRelease-1>",self.Rotate      )
        self.DrawButton       .bind("<ButtonRelease-1>",self.StartDraw   )
        self.CropButton       .bind("<ButtonRelease-1>",self.StartCroping)
        self.AdjustButton     .bind("<ButtonRelease-1>",self.EditAdjust  )
        self.FiltersButton    .bind("<ButtonRelease-1>",self.ApplyFilters)
        self.ClearButton      .bind("<ButtonRelease-1>",self.Clear       )
        self.UndoButton       .bind("<ButtonRelease-1>",self.Undo        )
        self.ExtractExifButton.bind("<ButtonRelease-1>",self.ExtractExif )

        self.ExtractExifButton.pack(side=BOTTOM)
        self.RotateButton     .pack(side=LEFT)
        self.DrawButton       .pack(side=LEFT)
        self.CropButton       .pack(side=LEFT)
        self.AdjustButton     .pack(side=LEFT)
        self.FiltersButton    .pack(side=LEFT)
        self.UndoButton       .pack(side=LEFT)
        self.ClearButton      .pack()

        self.ChangesSaved = False
        self.master.protocol("WM_DELETE_WINDOW", self.BeforeClosing)

        self.FilesTypesImport = [("All Picture file",("*.bmp","*.png","*.jpeg","*.jpg","*.jpe","*.ico","*.tiff",".*tif","*.webp")) ,("Bitmap Files","*.bmp"),("PNG (*.png)","*.png") , ("JPEG (*.jpg,*.jpeg,*.jpe)",("*.jpeg","*.jpg","*.jpe")) , ("ICO (*.ico)","*.ico") , ("WEBP (*.webp)","*.webp"),("TIFF",("*.tiff",".*tif"))]
        self.FilesTypesSave   = [("Bitmap Files","*.bmp"),("PNG (*.png)","*.png") , ("JPEG (*.jpg,*.jpeg,*.jpe)",("*.jpeg","*.jpg","*.jpe")) , ("ICO (*.ico)","*.ico") , ("WEBP (*.webp)","*.webp"),("TIFF",("*.tiff",".*tif"))]

        
    def NewPictureImported(self):
        filename = filedialog.askopenfilename( initialdir=path.join('C:\\','Users',getlogin(),'Desktop\\'),filetypes=self.FilesTypesImport)
        image = Image.open(filename)

        if image is not None:
            self.master.filename = filename
            self.master.OriginalImage = image.copy()
            self.master.EditedImage = image.copy()
            self.type = image.format
            self.master.viewimage.ShowImage()
            self.master.ImageIsSelected = True
    
    def SavePicture(self):
        if self.master.ImageIsSelected:
            SavedImage = self.master.EditedImage
            SavedImage.save(self.master.filename,quality=100, optimize=True)
            self.ChangesSaved = True
        else:
            messagebox.showinfo(title='Image Editor', message='Please import a picrure first.')
            self.NewPictureImported()
    

    def SavePictureAs(self):
        if self.master.ImageIsSelected:
            try:
                for i in range(len(self.FilesTypesSave)-1):
                    if (self.FilesTypesSave[i][0].find(self.type)) != -1:
                        Type = self.FilesTypesSave[i]
                        self.FilesTypesSave.pop(i)
                    else:
                        pass
                self.FilesTypesSave.insert(0,Type)
                Type = None
                filename = filedialog.asksaveasfilename(filetypes= self.FilesTypesSave,initialdir= path.join('C:\\','Users',getlogin(),'Desktop\\') )
                self.master.EditedImage.save(filename, quality=100, optimize=True)
                self.master.filename = filename
                self.ChangesSaved = True

            except ValueError as e:
                pass
        else:
            messagebox.showinfo(title='Image Editor', message='Please import a picrure first.')
            self.NewPictureImported()
    
    def Exit(self):
        self.BeforeClosing()      

    def Rotate(self,event):
        if self.winfo_containing(event.x_root, event.y_root) == self.RotateButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DisactivateDraw()
                if self.master.cropstatus:
                    self.master.viewimage.DisactivateCrop()
                self.master.rotate_frame = Rotate(master=self.master)
                self.master.rotate_frame.grab_set()
            else:
                messagebox.showinfo(title='Image Editor', message='Please import a picrure first.')
                self.NewPictureImported()

    def StartDraw(self,event):
        if self.winfo_containing(event.x_root, event.y_root) == self.DrawButton:
            if self.master.ImageIsSelected:
                if self.master.cropstatus:
                    self.master.viewimage.DisactivateCrop()
                if self.master.drawstatus:
                    self.master.viewimage.DisactivateDraw()
                else:
                    self.master.viewimage.StartDrawing()
            else:
                messagebox.showinfo(title='Image Editor', message='Please import a picrure first.')
                self.NewPictureImported()

    def StartCroping(self,event):
        if self.winfo_containing(event.x_root, event.y_root) == self.CropButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DisactivateDraw()
                if self.master.cropstatus:
                    self.master.viewimage.DisactivateCrop()
                else:
                    self.master.viewimage.StarCrop()
            else:
                messagebox.showinfo(title='Image Editor', message='Please import a picrure first.')
                self.NewPictureImported()


    def EditAdjust(self,event):
        if self.winfo_containing(event.x_root, event.y_root) == self.AdjustButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DisactivateDraw()
                if self.master.cropstatus:
                    self.master.viewimage.DisactivateCrop()
                self.master.adjust_frame = Adjust(master=self.master)
                self.master.adjust_frame.grab_set()
            else:
                messagebox.showinfo(title='Image Editor', message='Please import a picrure first.')
                self.NewPictureImported()

    def ApplyFilters(self,event):
        if self.winfo_containing(event.x_root, event.y_root) == self.FiltersButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DisactivateDraw()
                if self.master.cropstatus:
                    self.master.viewimage.DisactivateCrop()
                self.master.filters_frame = Filters(master=self.master)
                self.master.filters_frame.grab_set()  
            else:
                messagebox.showinfo(title='Image Editor', message='Please import a picrure first.')
                self.NewPictureImported()

    def Clear(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.ClearButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DisactivateDraw()
                if self.master.cropstatus:
                    self.master.viewimage.DisactivateCrop()
                self.master.EditedImage = self.master.OriginalImage.copy()
                self.master.viewimage.ClearCanvas()
            else:
                messagebox.showinfo(title='Image Editor', message='Please import a picrure first.')
                self.NewPictureImported()

    def Undo(self,event):
        if self.winfo_containing(event.x_root , event.y_root) == self.UndoButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DisactivateDraw()
                if self.master.cropstatus:
                    self.master.viewimage.DisactivateCrop()
                self.master.EditedImage =  self.master.BackUpImage
                self.master.viewimage.ClearCanvas()
            else:
                messagebox.showinfo(title='Image Editor', message='Please import a picrure first.')
                self.NewPictureImported()
                
    def ExtractExif(self,event):
        if self.winfo_containing(event.x_root , event.y_root) == self.ExtractExifButton:
            if self.master.ImageIsSelected:
                if self.master.drawstatus:
                    self.master.viewimage.DisactivateDraw()
                if self.master.cropstatus:
                    self.master.viewimage.DisactivateCrop()
                
                if self.master.ImageType in ('JPEG','WEBP','TIFF'):
                    try:
                        exif_dict = piexif.load(self.master.filename)
                        thumbnail = exif_dict.pop('thumbnail')
                        if thumbnail is not None:
                            with open(path.join('C:\\','Users',getlogin(),'AppData','Local','Temp','thumbnail.jpg'), 'wb') as f:
                                f.write(thumbnail)
                        with open(path.join('C:\\','Users',getlogin(),'Desktop\\','results.txt'), 'w') as f:
                            for ifd in exif_dict:
                                f.write(ifd+":")
                                f.write('\n')
                                for tag in exif_dict[ifd]:
                                    tag_name = piexif.TAGS[ifd][tag]["name"]+": "
                                    tag_value = exif_dict[ifd][tag]
                                
                                    if isinstance(tag_value, bytes):
                                        tag_value = tag_value.decode("utf-8")
                                    data = tag_name+str(tag_value)
                                    f.write(data)
                                    f.write("\n")
                                f.write('\n')
                        messagebox.showinfo(title='Image Editor', message='Data saved on '+path.join('C:\\','Users',getlogin(),'Desktop\\','results.txt'))
                    except ValueError:
                        messagebox.showinfo(title='Image Editor', message='The image has no exif')
                else:
                    messagebox.showinfo(title='Image Editor', message=' Only JPEG, WebP and TIFF files are supported.')
            else:
                messagebox.showinfo(title='Image Editor', message='Please import a picrure first.')
                self.NewPictureImported()

    def BeforeClosing(self):
        if self.master.ImageIsSelected:
            if self.ChangesSaved == False:
                test =  messagebox.askyesnocancel("Image Editor","Do you want to save changes?")
                if test:
                    self.SavePictureAs()
                if test == False:
                    self.master.destroy()
        else:
            self.master.destroy()
           