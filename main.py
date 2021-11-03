from tkinter import *
from tkinter import ttk
from editingbuttons import EditingButtons
from showimage import ShowImage
class Main(Tk):
    def __init__(self):
        
        self.filename = ""
        self.OriginalImage = None
        self.EditedImage = None
        self.ImageIsSelected = False


        Tk.__init__(self)
        self.title('Image Editor')
        self.iconphoto(True,PhotoImage(file="icon.png"))
        self.geometry(f'{self.winfo_screenwidth()}x{self.winfo_screenheight()}')
        self.buttons = EditingButtons(master=self)
        self.buttons.pack(pady=25)
        
        separator = ttk.Separator(master=self, orient=HORIZONTAL)
        separator.pack(fill=X ,padx=10 , pady=20)

        self.viewimage = ShowImage(master=self)
        self.viewimage.pack(fill=BOTH ,padx=20,expand=1)
        
window = Main()
window.mainloop()

