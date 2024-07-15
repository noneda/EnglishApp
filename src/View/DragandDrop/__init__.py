import tkinter as tk
import random
from MainWindow import Form

class DragDropHandler(tk.Label):
    text : str
    pos : tuple
    
    canvas = Form
    labelSave : tk.Canvas.create_rectangle
    drop_zone : tk.Canvas.create_rectangle

    pastel_colors = [
        'alice blue',             # #f0f8ff
        'antique white',          # #faebd7
        'blanched almond',        # #ffebcd
        'cornsilk',               # #fff8dc
        'lavender',               # #e6e6fa
        'light blue',             # #add8e6
        'light coral',            # #f08080
        'light cyan',             # #e0ffff
        'light goldenrod yellow', # #fafad2
        'light pink'              # #ffb6c1
    ]
    
    drag_data = {
        'x ': int,
        'y' : int,
        'item' : None
    }

    @staticmethod
    def configs(cls : tk.Label):
        cls.config(
            text = cls.text,
            bg = random.choice(cls.pastel_colors)
        )
        cls.bind(
            '<ButtonPress-1>', 
             cls.drag_start
        )
        cls.bind(
            '<B1-Motion>', 
            cls.drag_motion
        )
        cls.bind(
            '<ButtonRelease-1>',
            cls.drag_end
        )

    def __init__(self, master : tk.Tk, txt: str, canva : Form, dropZone: tk.Canvas.create_rectangle, pos : tuple ,**kwargs):
        super().__init__(master, **kwargs)
        self.text = txt
        self.canvas = canva
        self.pos = pos

        self.configs(self)
        self.labelSave = self.canvas.create_window(
            pos[0],
            pos[1],
            window= self, 
            anchor='nw'
        )
        self.drop_zone = dropZone

    def drag_start(self , e):
        self.drag_data['item'] = self.labelSave
        self.drag_data['x'] = e.x_root
        self.drag_data['y'] = e.y_root

    def drag_motion(self, e):
        delta_x = e.x_root - self.drag_data['x']
        delta_y = e.y_root - self.drag_data['y']

        self.canvas.move(
            self.drag_data['item'],
            delta_x, 
            delta_y
        )

        self.drag_data['x'] = e.x_root
        self.drag_data['y'] = e.y_root

    def drag_end(self, e):
        x1, y1, x2, y2 = self.canvas.coords(self.drop_zone)

        label_x, label_y = self.canvas.coords(self.labelSave)
        label_width = self.winfo_width()
        label_height = self.winfo_height()
        label_center_x = label_x + label_width / 2
        label_center_y = label_y + label_height / 2

        if x1 <= label_center_x <= x2 and y1 <= label_center_y <= y2:
            print("Drop válido en la zona especificada.")
        else:
            print("El drop no está en la zona especificada. Regresando al inicio.")
            self.canvas.coords(self.drag_data['item'], self.pos[0], self.pos[1])
        
        self.drag_data['item'] = None