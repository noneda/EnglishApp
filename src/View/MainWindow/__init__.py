import tkinter  as tk

class Form(tk.Canvas):
    
    @staticmethod
    def configs(cls):
        cls.config(
            width=500,
            height=300,
            bg = 'white'
        )

    def __init__(self, master : tk.Tk, **kwargs):
        super().__init__(master, **kwargs)
        self.configs(self)
        print(
            "Form : x = 500, y = 300" 
        )


