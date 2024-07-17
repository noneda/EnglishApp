import tkinter  as tk

class Form(tk.Canvas):
    
    @staticmethod
    def configs(cls : tk.Canvas):
        cls.config(
            width=500,
            height=300,
            bg = 'white'
        )

        cls.pack(
            expand=True,
            fill='both'
        )

    def __init__(self, master : tk.Tk, **kwargs):
        super().__init__(master, **kwargs)
        self.configs(self)

            
    def add_frame(self, frame : tk.Frame, name : str):
        obj = frame(self)
        self.frames[name] = obj

        self.create_window(
            0,
            0,
            anchor= "nw",
            window=frame
        )

    def show_frame(self, name : str):
        frame : tk.Frame
        frame = self.frames.get(name)
        if frame:
            frame.tkraise()

