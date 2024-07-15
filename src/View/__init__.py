import tkinter as tk
from MainWindow import Form
from DragandDrop import DragDropHandler

class Main(tk.Tk):
    form: Form
    labels: dict 

    @staticmethod
    def configs(cls: tk.Tk):
        cls.title("Doulingo for poor")
        cls.form = Form(cls)
        cls.form.pack()

    def __init__(self):
        super().__init__()
        self.configs(self)
        dropZone = self.form.create_rectangle(
            50,
            50,
            450,
            100,
        )
        self.labels = {}  
        pos_x , pos_y = 95,  125
        for i in range(1, 6 + 1):
            label = DragDropHandler(
                master=self,
                txt=f"TouchMe {i}",
                canva=self.form,
                dropZone=dropZone,
                pos = (pos_x, pos_y)
            )
            self.labels[f"label{i}"] = label  
            pos_x  += 125
            if(i % 3 == 0):
                pos_x = 95
                pos_y += 50
            print("x " + str(pos_x) + " y " + str(pos_y))

if __name__ == "__main__":
    master = Main()
    master.mainloop()

