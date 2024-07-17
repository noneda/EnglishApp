import tkinter as tk

class SolveFrame(tk.Frame):

    @staticmethod
    def configs(cls : tk.Frame):
        cls.config(
            width= 500,
            height= 300,
        )
        cls.grid_propagate(False)
        cls.pack_propagate(False)


    def __init__(self, master : tk.Canvas, **kwargs):
        super().__init__(master= master, **kwargs)
        