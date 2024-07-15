import tkinter as tk

class RoundedCanvas(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

    def create_rounded_rectangle(self, x1, y1, x2, y2, corner_radius, bg , outline, width=2):
        # Dibujar el rectángulo de fondo
        self.create_rectangle(x1, y1 + corner_radius, x2, y2 - corner_radius, fill=bg, outline="")

        # Dibujar los arcos en las esquinas para simular los bordes redondeados
        self.create_arc(x1, y1, x1 + 2 * corner_radius, y1 + 2 * corner_radius, start=90, extent=90, style=tk.ARC, outline=outline, width=width)
        self.create_arc(x2 - 2 * corner_radius, y1, x2, y1 + 2 * corner_radius, start=0, extent=90, style=tk.ARC, outline=outline, width=width)
        self.create_arc(x1, y2 - 2 * corner_radius, x1 + 2 * corner_radius, y2, start=180, extent=90, style=tk.ARC, outline=outline, width=width)
        self.create_arc(x2 - 2 * corner_radius, y2 - 2 * corner_radius, x2, y2, start=270, extent=90, style=tk.ARC, outline=outline, width=width)

        # Dibujar las líneas horizontales del borde redondeado
        self.create_line(x1 + corner_radius, y1, x2 - corner_radius, y1, fill=outline, width=width)
        self.create_line(x1 + corner_radius, y2, x2 - corner_radius, y2, fill=outline, width=width)

        # Dibujar las líneas verticales del borde redondeado
        self.create_line(x1, y1 + corner_radius, x1, y2 - corner_radius, fill=outline, width=width)
        self.create_line(x2, y1 + corner_radius, x2, y2 - corner_radius, fill=outline, width=width)

    def create_rectangle(self, x1, y1, x2, y2, **kwargs):
        # Verificar si se proporciona el argumento corner_radius
        if 'corner_radius' in kwargs:
            corner_radius = kwargs.pop('corner_radius')
            self.create_rounded_rectangle(x1, y1, x2, y2, corner_radius, **kwargs)
        else:
            super().create_rectangle(x1, y1, x2, y2, **kwargs)

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    canvas = RoundedCanvas(root, width=500, height=300)
    canvas.pack()

    # Creación de un rectángulo con bordes redondeados
    canvas.create_rectangle(50, 50, 250, 150, corner_radius=20, bg='#EAECEE', outline='#D6DBDF', width=2)

    root.mainloop()
