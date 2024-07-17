import tkinter as tk

class Start(tk.Frame):

    frames : dict

    @staticmethod
    def configs(cls):
        cls.title("Start App")
        
    def __init__(self):
        super().__init__()
