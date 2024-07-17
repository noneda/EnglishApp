import tkinter as tk
from Frames import SolveFrame
from MainWindow import Form
from DragandDrop import DragDropHandler
from Controller.GetOration import Oration


class Dou(SolveFrame):
    form: Form
    labels: dict 
    dropZone : tk.Canvas.create_rectangle

    def __init__(self):
        super().__init__()
        self.configs(self)
        self.dropZone = self.form.create_rectangle(
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
                dropZone=self.dropZone,
                pos = (pos_x, pos_y)
            )
            self.labels[f"label{i}"] = label  
            pos_x  += 125
            if(i % 3 == 0):
                pos_x = 95
                pos_y += 50
            print("x " + str(pos_x) + " y " + str(pos_y))

        self.generate_button = tk.Button(self, text="Generar Oración", command=self.display_sentence)
        self.generate_button.pack(pady=20)

    def display_sentence(self):
        obj = Oration()
        sentence = obj.OrdenBySentences( 
            drop_zone= self.form.coords(self.dropZone), 
            labels= self.labels
            )
        new_window = tk.Toplevel(self)
        new_window.title("Generated Sentence")
        label = tk.Label(new_window, text=sentence, wraplength=400, padx=20, pady=20)
        label.pack()
