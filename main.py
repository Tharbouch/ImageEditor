from tkinter import *

class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Image Editor')
        self.iconphoto(True,PhotoImage(file="icon.png"))
        self.geometry(f'{self.winfo_screenwidth()}x{self.winfo_screenheight()}')
        
window = Main()
window.mainloop()

